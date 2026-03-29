from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def alexa():
    data = request.json

    try:
        request_type = data["request"]["type"]

        # 👉 CUANDO ABRES LA SKILL
        if request_type == "LaunchRequest":
            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": "Estamos en Asistente C"
                    },
                    "shouldEndSession": False
                }
            })

        # 👉 CUANDO DICES UN COMANDO
        if request_type == "IntentRequest":
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
                "text": "Error"
            }
        }
    })


# 👉 IMPORTANTE PARA RENDER
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)