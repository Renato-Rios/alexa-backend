from flask import jsonify
from views.apl_templates import pantalla_principal
from services.alexa_service import procesar_accion

def manejar_request(data):
    interfaces = data["context"]["System"]["device"]["supportedInterfaces"]

    tiene_apl = "Alexa.Presentation.APL" in interfaces

    request_type = data["request"]["type"]

    # 🔥 CUANDO ABRES LA SKILL
    if request_type == "LaunchRequest":

        if tiene_apl:
            mensaje = "Detecté pantalla"
        else:
            mensaje = "No detecté pantalla"

        return jsonify({
            "version": "1.0",
            "response": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": mensaje
                },

                # 👇 SOLO si hay pantalla mandamos UI
                "directives": [
                    {
                        "type": "Alexa.Presentation.APL.RenderDocument",
                        "token": "main",
                        "document": pantalla_principal()
                    }
                ] if tiene_apl else [],

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