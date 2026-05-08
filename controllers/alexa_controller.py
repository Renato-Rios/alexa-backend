from flask import jsonify
from views.apl_templates import pantalla_principal
from views.learn.home_learn import learn_gui
from views.learn.fase_1 import fase_1_gui
from views.music.home_music import music_gui
from services.alexa_service import procesar_accion
import psycopg2
import requests

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
        # Spotify responde con un 204 si todo sale bien
        response = requests.put(url, headers=headers, json=data)
        return response.status_code
    except Exception as e:
        print(f"Error en Spotify API: {e}")
        return 500

#funcion encargada de obtener informacion de la base de datos para fase 1
def get_learning_content():
    conn = psycopg2.connect(
        host="dpg-d7klgul7vvec73cebok0-a.oregon-postgres.render.com",
        database="asistentec",
        user="admin",
        password="HGjBPcY5YLIWaVtBNzWsvtmns6NAO8fN",
        port=5432
    )

    cursor = conn.cursor()

    cursor.execute("""
        SELECT w.word, w.phonetic, i.url
        FROM words w
        JOIN images i ON w.id = i.word_id
        WHERE i.patient_id = 1
        ORDER BY RANDOM()
        LIMIT 1;
    """)

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return {
            "word": result[0],
            "phonetic": result[1],
            "image": result[2]
        }
    else:
        return None

def manejar_request(data):
    # Extraer información básica
    tipo = data["request"]["type"]
    datasources = {}

    # Caso 1: Inicio de la Skill
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

    # Caso 2: Interacción con botones (UserEvent)
    if tipo == "Alexa.Presentation.APL.UserEvent":
        argumentos = data["request"].get("arguments", [])
        accion = argumentos[0] if argumentos else None
        
        documento = pantalla_principal()
        texto = "Cargando selección"

        # --- LÓGICA DE NAVEGACIÓN ---
        if accion == "aprender":
            texto = "Entrando a aprender"
            documento = learn_gui()
            
        elif accion == "musica":
            texto = "Entrando a música"
            documento = music_gui()
            
        elif accion == "fase1":
            contenido = get_learning_content()
            if contenido:
                texto = f"La palabra es {contenido['word']}"
                documento = fase_1_gui()
                datasources = {
                    "datosFase": {
                        "type": "object",
                        "word": contenido['word'],
                        "image": contenido['image'],
                        "phonetic": contenido['phonetic']
                    }
                }
            else:
                texto = "No encontré contenido"
                documento = learn_gui()

        # --- 🔷 LÓGICA DE SPOTIFY ---
        elif accion in ["playlist_mama", "playlist_renato", "playlist_oliver"]:
            access_token = data["context"]["System"]["user"].get("accessToken")
            
            # Si no hay vinculación, mandamos la tarjeta especial
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

            # Diccionario con tus IDs de 22 caracteres
            playlists = {
                "playlist_mama": "0KQyC28P9808r0oKKNgHvp",
                "playlist_renato": "37i9dQZF1DXcBWIGvYBM3s",
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

        # Respuesta para UserEvent
        return jsonify({
            "version": "1.0",
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

    # Caso 3: Comandos de voz (IntentRequest)
    if tipo == "IntentRequest":
        intent = data["request"]["intent"]["name"]
        
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

        # ... (Help, Cancel, Stop intents igual que antes)
        
    # Ayuda
        if intent == "AMAZON.HelpIntent":
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "En esta skill puedes aprender sobre nuestro lenguaje y escuchar música, con solo decir Alexa, vamos a aprender"+
                            "o Alexa, vamos a escuchar música se activarán las funciones correspondientes"
                    },
                    "shouldEndSession": False
                }
            })
        #Salida
        if intent == "AMAZON.CancelIntent" or intent == "AMAZON.StopIntent":
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
            "outputSpeech": {"type": "PlainText", "text": "Lo siento, hubo un error"},
            "shouldEndSession": False
        }
    })
