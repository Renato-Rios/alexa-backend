from flask import jsonify
from views.apl_templates import pantalla_principal
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

    # 🔥 Botones
    if tipo == "Alexa.Presentation.APL.UserEvent":
        accion = data["request"]["arguments"][0]
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

    # 🟡 Intent
    if tipo == "IntentRequest":
        intent = data["request"]["intent"]["name"]

        if intent == "HablarIntent":
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "Hola mundo"
                    },
                    "shouldEndSession": False
                }
            })

    return jsonify({
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Error"
            }
        }
    })