from flask import jsonify
from views.apl_templates import pantalla_principal
from views.learn.home_learn import learn_gui
from views.learn.fase_1 import fase_1_gui
from views.music.home_music import music_gui
from services.alexa_service import procesar_accion
import psycopg2

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
    interfaces = data["context"]["System"]["device"]["supportedInterfaces"]
    tiene_apl = "Alexa.Presentation.APL" in interfaces

    tipo = data["request"]["type"]

    if tipo == "LaunchRequest":

        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Estamos en Asistente C"
                },

                "directives": [
                    {
                        "type": "Alexa.Presentation.APL.RenderDocument",
                        "token": "main",

                        # 🔥 ESTA LÍNEA FALTABA
                        "document": pantalla_principal(),

                        # 🔥 AGREGA ESTO (IMPORTANTE)
                        "datasources": {}
                    }
                ],

                "shouldEndSession": False
            }
        })

    # Botones
    if tipo == "Alexa.Presentation.APL.UserEvent":
        accion = data["request"]["arguments"][0]
        if not accion:
            texto = "No entendí a dónde quieres ir"
        elif accion == "aprender":
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
                    "payload": {
                        "word": contenido['word'],
                        "image": contenido['image'],
                        "phonetic": contenido['phonetic']
                    }
                }
            else:
                texto = "No encontré contenido"
                documento = learn_gui()
                datasources = {}
        else:
            texto = "Opción no válida"
            documento = pantalla_principal()

        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": texto
                },
                "directives": [
                    {
                    "type": "Alexa.Presentation.APL.RenderDocument",
                    "token": "cambio",
                    "document": documento,
                    "datasources": datasources
                    }
                ],
                "shouldEndSession": False
            }
        })

    #Intent
    if tipo == "IntentRequest":
        intent = data["request"]["intent"]["name"]

        if intent == "HablarIntent":
            slots = data["request"]["intent"].get("slots", {})
            accion = slots.get("accion", {}).get("value")  # 🔥 ESTA LÍNEA FALTABA

            if not accion:
                texto = "No entendí a dónde quieres ir"
            else:
                texto = procesar_accion(accion)

            return jsonify({
                "version": "1.0",
                "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": texto
            },
            "shouldEndSession": False
                }
            })
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
    
    #Cada vez que no se entienda la petición
    return jsonify({
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Error"
            },
            "shouldEndSession": False
        }
    })