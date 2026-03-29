from flask import jsonify
from views.apl_templates import pantalla_principal
from services.alexa_service import procesar_accion

def manejar_request(data):
    tipo = data["request"]["type"]

    # 🟢 Launch
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
                        "token": "pantallaPrincipal",
                        "document": pantalla_principal()
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