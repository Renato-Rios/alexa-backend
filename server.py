from flask import Flask, request
from controllers.alexa_controller import manejar_request

app = Flask(__name__)

@app.route("/", methods=["POST"])
def alexa():
    data = request.json
    return manejar_request(data)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)