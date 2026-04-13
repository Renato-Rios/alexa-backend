from flask import jsonify
from views.apl_templates import pantalla_principal
from views.learn.home_learn import learn_gui
from views.music.home_music import music_gui
from services.alexa_service import procesar_accion

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
                    "datasources": {}
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
                        "text": "En esta skill puedes aprender y escuchar música, con solo decir Alexa, vamos a aprender"+
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