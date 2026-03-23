from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def alexa():
    data = request.json

    try:
        intent = data["request"]["intent"]["name"]

        if intent == "HablarIntent":
            mensaje = data["request"]["intent"]["slots"]["mensaje"]["value"]

            print("Alexa dijo:", mensaje)

            return jsonify({
                "version": "1.0",
                "response": {
                    "outputSpeech": {
                        "type": "PlainText",
                        "text": mensaje
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
                "text": "No entendí"
            },
            "shouldEndSession": False
        }
    })

# 👇 IMPORTANTE PARA RENDER
if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)