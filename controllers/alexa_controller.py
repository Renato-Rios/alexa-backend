import time
import requests
import psycopg2
import numpy as np
import Levenshtein  # Recuerda instalarlo en tu entorno/Render: pip install python-Levenshtein
from flask import jsonify
from views.apl_templates import pantalla_principal
from views.learn.home_learn import learn_gui
from views.learn.fase_1 import fase_1_gui
from views.music.home_music import music_gui
from services.alexa_service import procesar_accion

# =====================================================================
# 🛠️ FUNCIONES AUXILIARES: CONEXIÓN, PERCEPTRÓN Y LOGICA DE APRENDIZAJE
# =====================================================================

def get_db_connection():
    """Centraliza la conexión a PostgreSQL para evitar repetir credenciales."""
    return psycopg2.connect(
        host="dpg-d8e7pme8bjmc73asb3p0-a.oregon-postgres.render.com",
        database="asistentec_ev22",
        user="renato",
        password="oXjjvt32e0qErXXoeJtpPKqPlZqAULCz",
        port=5432
    )

def reconocer_porcentaje(features, archivo_modelo="modelo.dat"):
    """Evalúa las características mediante el perceptrón continuo con Sigmoide."""
    try:
        with open(archivo_modelo, "r") as f:
            lineas = f.readlines()
            w = np.array(list(map(float, lineas[0].split())))
            theta = float(lineas[1])
        
        h = np.dot(features, w) - theta  
        porcentaje_acierto = 1 / (1 + np.exp(-h))
        return float(porcentaje_acierto * 100)
    except Exception as e:
        print(f"Error en Perceptrón: {e}")
        return 50.0  # Fallback seguro por si el archivo no se encuentra

def obtener_siguiente_palabra(patient_id, session_attributes):
    """
    Aplica el patrón 2-1 basándose en el promedio histórico de intentos.
    Garantiza que ninguna palabra se repita hasta haber recorrido todo el vocabulario.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Obtener el umbral del paciente
    cursor.execute("SELECT target_threshold FROM caregiver_config WHERE patient_id = %s", (patient_id,))
    res = cursor.fetchone()
    threshold = res[0] if res else 75.0
    
    # 2. Obtener TODAS las palabras asignadas al paciente con su PROMEDIO de acierto histórico
    cursor.execute("""
        SELECT w.id, w.word, w.phonetic, i.url, AVG(COALESCE(a.accuracy_percentage, 0)) as promedio_acierto
        FROM words w
        JOIN images i ON w.id = i.word_id
        LEFT JOIN patient_attempts a ON w.id = a.word_id AND a.patient_id = %s
        WHERE i.patient_id = %s
        GROUP BY w.id, w.word, w.phonetic, i.url;
    """, (patient_id, patient_id))
    
    todas_las_palabras = cursor.fetchall()
    cursor.close()
    conn.close()
    
    if not todas_las_palabras:
        return None

    # 3. Recuperar el historial de palabras ya vistas en esta ronda desde la sesión de Alexa
    vistas = session_attributes.get("palabras_vistas_historico", [])
    
    # Si ya vimos todas las palabras de la BD, reiniciamos la lista negra para una nueva ronda
    if len(vistas) >= len(todas_las_palabras):
        vistas = []
        session_attributes["palabras_vistas_historico"] = []

    # 4. Clasificar las palabras DISPONIBLES (filtrando las que ya se vieron)
    dificiles_disponibles = []
    faciles_disponibles = []
    
    for p in todas_las_palabras:
        p_id = p[0]
        # Si la palabra ya fue vista en este ciclo, la ignoramos temporalmente
        if p_id in vistas:
            continue
            
        # Formateamos el diccionario de la palabra
        p_dict = {"id": p_id, "word": p[1], "phonetic": p[2], "image": p[3], "promedio": float(p[4])}
        
        # Clasificación por promedio histórico vs umbral esperado
        if p_dict["promedio"] < threshold:
            dificiles_disponibles.append(p_dict)
        else:
            faciles_disponibles.append(p_dict)

    # 5. Determinar qué tipo de palabra toca según el patrón (2 difíciles, 1 fácil)
    contador = session_attributes.get("contador_palabras", 1)
    toca_facil = (contador % 3 == 0)
    
    palabra_elegida = None

    if toca_facil:
        if faciles_disponibles:
            palabra_elegida = faciles_disponibles[np.random.choice(len(faciles_disponibles))]
        else:
            if dificiles_disponibles:
                palabra_elegida = dificiles_disponibles[np.random.choice(len(dificiles_disponibles))]
    else:
        if dificiles_disponibles:
            palabra_elegida = dificiles_disponibles[np.random.choice(len(dificiles_disponibles))]
        else:
            if faciles_disponibles:
                palabra_elegida = faciles_disponibles[np.random.choice(len(faciles_disponibles))]

    # 6. Si encontramos una palabra, actualizar registros de exclusión en la sesión
    if palabra_elegida:
        vistas.append(palabra_elegida["id"])
        session_attributes["palabras_vistas_historico"] = vistas
        return palabra_elegida
        
    return None

def play_spotify_playlist(token, playlist_id):
    """Envía la orden a la API de Spotify usando el token de vinculación."""
    url = "https://api.spotify.com/v1/me/player/play"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    data = {
        "context_uri": f"spotify:playlist:{playlist_id}"
    }
    try:
        response = requests.put(url, headers=headers, json=data)
        return response.status_code
    except Exception as e:
        print(f"Error en Spotify API: {e}")
        return 500


# =====================================================================
# 🧠 CEREBRO PRINCIPAL: MANEJAR REQUEST
# =====================================================================

def manejar_request(data):
    tipo = data["request"]["type"]
    
    session_attributes = data.get("session", {}).get("attributes", {})
    datasources = {}
    patient_id = 1  # ID fijo del paciente asignado (Andrea)

    # -----------------------------------------------------------------
    # CASO 1: Inicio de la Skill (LaunchRequest)
    # -----------------------------------------------------------------
    if tipo == "LaunchRequest":
        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Estamos en Asistente C"
                },
                "directives": [{
                    "type": "Alexa.Presentation.APL.RenderDocument",
                    "token": "main_token",
                    "document": pantalla_principal(),
                    "datasources": {}
                }],
                "shouldEndSession": False
            }
        })

    # -----------------------------------------------------------------
    # CASO 2: Interacción con botones de la pantalla (UserEvent)
    # -----------------------------------------------------------------
    if tipo == "Alexa.Presentation.APL.UserEvent":
        argumentos = data["request"].get("arguments", [])
        accion = argumentos[0] if argumentos else None
        
        documento = pantalla_principal()
        texto = "Cargando selección"

        if accion == "aprender":
            texto = "Entrando a aprender"
            documento = learn_gui()
            
        elif accion == "musica":
            texto = "Entrando a música"
            documento = music_gui()
            
        elif accion == "fase1":
            contenido = obtener_siguiente_palabra(patient_id, session_attributes)
            if contenido:
                texto = f"Mira la pantalla, ¿puedes decir la palabra {contenido['word']}?"
                documento = fase_1_gui()
                datasources = {
                    "datosFase": {
                        "type": "object",
                        "word": contenido['word'],
                        "image": contenido['image'],
                        "phonetic": contenido['phonetic']
                    }
                }
                session_attributes["palabra_actual_id"] = contenido["id"]
                session_attributes["palabra_actual_texto"] = contenido["word"]
                session_attributes["timestamp_inicio"] = time.time()
            else:
                texto = "No encontré contenido configurado en la base de datos."
                documento = learn_gui()

        elif accion in ["playlist_mama", "playlist_renato", "playlist_oliver"]:
            access_token = data["context"]["System"]["user"].get("accessToken")
            
            if not access_token:
                return jsonify({
                    "version": "1.0",
                    "response": {
                        "outputSpeech": {
                            "type": "PlainText", 
                            "text": "Para escuchar música, vincula tu cuenta de Spotify en la app de Alexa."
                        },
                        "card": {"type": "LinkAccount"}
                    }
                })

            playlists = {
                "playlist_mama": "6s4aGjq9b42OP4nMGNCLUu",
                "playlist_renato": "2U7tqVQDraESQSOTKgVSKA",
                "playlist_oliver": "3PDxZ7MCDaJ07Kvz47MQIq"
            }

            playlist_id = playlists.get(accion)
            status = play_spotify_playlist(access_token, playlist_id)

            if status == 204:
                texto = "¡Claro! Disfruta la música."
            elif status == 404:
                texto = "No encontré un dispositivo activo. Abre Spotify en tu Alexa o celular un momento."
            elif status == 403:
                texto = "Spotify me dice que necesitas una cuenta Premium para controlar la música así."
            else:
                texto = "Hubo un problema al conectar con Spotify."
            
            documento = music_gui()

        return jsonify({
            "version": "1.0",
            "sessionAttributes": session_attributes,
            "response": {
                "outputSpeech": {"type": "PlainText", "text": texto},
                "directives": [{
                    "type": "Alexa.Presentation.APL.RenderDocument",
                    "token": "nav_token",
                    "document": documento,
                    "datasources": datasources
                }],
                "shouldEndSession": False
            }
        })

    # -----------------------------------------------------------------
    # CASO 3: Procesamiento por comandos de voz (IntentRequest)
    # -----------------------------------------------------------------
    if tipo == "IntentRequest":
        intent = data["request"]["intent"]["name"]
        
        if intent == "RespuestaPalabraIntent":
            slots = data["request"]["intent"].get("slots", {})
            palabra_dicha = slots.get("palabra_usuario", {}).get("value", "")
            
            palabra_real_texto = session_attributes.get("palabra_actual_texto")
            palabra_real_id = session_attributes.get("palabra_actual_id")
            timestamp_inicio = session_attributes.get("timestamp_inicio", time.time())
            
            if not palabra_real_texto:
                return jsonify({
                    "version": "1.0",
                    "response": {
                        "outputSpeech": {"type": "PlainText", "text": "Lo siento, perdí el hilo de la práctica. Regresa al menú principal."},
                        "shouldEndSession": False
                    }
                })
            
            tiempo_respuesta = time.time() - timestamp_inicio
            score_similitud = Levenshtein.ratio(palabra_real_texto.lower(), palabra_dicha.lower())
            
            features = [score_similitud, tiempo_respuesta]
            porcentaje = reconocer_porcentaje(features)
            
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO patient_attempts (patient_id, word_id, word_said, accuracy_percentage, response_time)
                VALUES (%s, %s, %s, %s, %s)
            """, (patient_id, palabra_real_id, palabra_dicha, porcentaje, tiempo_respuesta))
            
            cursor.execute("SELECT target_threshold FROM caregiver_config WHERE patient_id = %s", (patient_id,))
            res = cursor.fetchone()
            threshold = res[0] if res else 75.0
            conn.commit()
            cursor.close()
            conn.close()
            
            if porcentaje >= threshold:
                # Incrementamos el contador para que avance en el patrón 2-1
                session_attributes["contador_palabras"] = session_attributes.get("contador_palabras", 1) + 1
                
                # 1. Buscamos la siguiente palabra PRIMERO para poder usar su texto en el mensaje de voz
                siguiente = obtener_siguiente_palabra(patient_id, session_attributes)
                
                if siguiente:
                    # 🛠️ FIJACIÓN CRÍTICA: Guardamos los datos de la nueva palabra en la sesión
                    session_attributes["palabra_actual_id"] = siguiente["id"]
                    session_attributes["palabra_actual_texto"] = siguiente["word"]
                    session_attributes["timestamp_inicio"] = time.time()  # Reseteamos el cronómetro
                    
                    # 🗣️ Modificamos el texto para que anuncie dinámicamente la siguiente palabra
                    texto_alexa = f"¡Excelente! Conseguiste un {int(porcentaje)} por ciento de acierto. ¡Vamos a la siguiente palabra! Intenta decir: {siguiente['word']}."
                    
                    return jsonify({
                        "version": "1.0",
                        "sessionAttributes": session_attributes,
                        "response": {
                            "outputSpeech": {"type": "PlainText", "text": texto_alexa},
                            "directives": [{
                                "type": "Alexa.Presentation.APL.RenderDocument",
                                "token": "fase_token",
                                "document": fase_1_gui(),
                                "datasources": {
                                    "datosFase": {
                                        "type": "object",
                                        "word": siguiente['word'],
                                        "image": siguiente['image'],
                                        "phonetic": siguiente.get('phonetic', '')
                                    }
                                }
                            }],
                            "shouldEndSession": False
                        }
                    })
                else:
                    # Si ya no quedan palabras en la BD (caso extremo o fin de ronda)
                    return jsonify({
                        "version": "1.0",
                        "sessionAttributes": session_attributes,
                        "response": {
                            "outputSpeech": {"type": "PlainText", "text": f"¡Increíble! Conseguiste un {int(porcentaje)} por ciento de acierto y completaste todas las palabras disponibles de esta ronda."},
                            "shouldEndSession": False
                        }
                    })
            else:
                texto_alexa = f"Te escuché decir {palabra_dicha}. Tuviste un {int(porcentaje)} por ciento de acierto. Vamos a practicarla de nuevo: Di, {palabra_real_texto}."
                session_attributes["timestamp_inicio"] = time.time()
                
                return jsonify({
                    "version": "1.0",
                    "sessionAttributes": session_attributes,
                    "response": {
                        "outputSpeech": {"type": "PlainText", "text": texto_alexa},
                        "shouldEndSession": False
                    }
                })

        if intent == "HablarIntent":
            slots = data["request"]["intent"].get("slots", {})
            accion = slots.get("accion", {}).get("value")
            texto = procesar_accion(accion) if accion else "No entendí a dónde quieres ir"
            
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {"type": "PlainText", "text": texto},
                    "shouldEndSession": False
                }
            })
        
        if intent == "AMAZON.HelpIntent":
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "En esta skill puedes aprender sobre nuestro lenguaje y escuchar música..."
                    },
                    "shouldEndSession": False
                }
            })
            
        if intent in ["AMAZON.CancelIntent", "AMAZON.StopIntent"]:
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "Eso es todo por ahora, cerrando asistente C"
                    },
                    "shouldEndSession": True
                }
            })

    return jsonify({
        "version": "1.0",
        "response": {
            "outputSpeech": {"type": "PlainText", "text": "Lo siento, opción no reconocida por Asistente C."},
            "shouldEndSession": False
        }
    })