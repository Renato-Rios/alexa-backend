from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def alexa():
    data = request.json

    try:
        tipo = data["request"]["type"]

        # 🟢 CUANDO ABRES LA SKILL
        if tipo == "LaunchRequest":
            return jsonify(respuesta_con_pantalla())

        # 🔥 CUANDO PICAS BOTONES (APL)
        if tipo == "Alexa.Presentation.APL.UserEvent":
            accion = data["request"]["arguments"][0]

            if accion == "musica":
                texto = "Reproduciendo música"

            elif accion == "aprender":
                texto = "Entrando a modo aprendizaje"

            else:
                texto = "No entendí el botón"

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

        # 🟡 INTENTS (VOZ)
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

    except Exception as e:
        print("Error:", e)

    return jsonify({
        "version": "1.0",
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Error en el servidor"
            }
        }
    })


# 🎨 PANTALLA ALEXA (APL)
def respuesta_con_pantalla():
    return {
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
                    "document": {
                        "type": "APL",
                        "version": "1.7",
                        "mainTemplate": {
                            "parameters": ["payload"],
                            "items": [
                                {
                                    "type": "Container",
                                    "direction": "column",
                                    "items": [
                                        {
                                            "type": "Text",
                                            "text": "Asistente C",
                                            "fontSize": "60dp",
                                            "horizontalAlignment": "center"
                                        },
                                        {
                                            "type": "TouchWrapper",
                                            "onPress": {
                                                "type": "SendEvent",
                                                "arguments": ["musica"]
                                            },
                                            "item": {
                                                "type": "Text",
                                                "text": "🎵 Música",
                                                "fontSize": "40dp"
                                            }
                                        },
                                        {
                                            "type": "TouchWrapper",
                                            "onPress": {
                                                "type": "SendEvent",
                                                "arguments": ["aprender"]
                                            },
                                            "item": {
                                                "type": "Text",
                                                "text": "📘 Aprender",
                                                "fontSize": "40dp"
                                            }
                                        }
                                    ]
                                }
                            ]
                        }
                    }
                }
            ],
            "shouldEndSession": False
        }
    }


# 🔴 NECESARIO PARA RENDER
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)