import os
from flask import Flask, request, jsonify
import nacl.signing
import nacl.exceptions
import requests

app = Flask(__name__)

PUBLIC_KEY = os.getenv("PUBLIC_KEY")


def verify_signature(req):
    signature = req.headers.get("X-Signature-Ed25519")
    timestamp = req.headers.get("X-Signature-Timestamp")

    body = req.data.decode("utf-8")

    try:
        verify_key = nacl.signing.VerifyKey(bytes.fromhex(PUBLIC_KEY))
        verify_key.verify(
            (timestamp + body).encode(),
            bytes.fromhex(signature)
        )
        return True

    except nacl.exceptions.BadSignatureError:
        return False


@app.route("/", methods=["POST"])
def interactions():

    if not verify_signature(request):
        return "invalid request", 401

    data = request.json

    # Discord verification
    if data["type"] == 1:
        return jsonify({"type": 1})

    # Slash command
    if data["type"] == 2:

        command = data["data"]["name"]

        if command == "echo":
            message = data["data"]["options"][0]["value"]

            return jsonify({
                "type": 4,
                "data": {
                    "content": message
                }
            })

    return jsonify({})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
