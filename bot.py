import os
from flask import Flask, request, jsonify
import nacl.signing
import nacl.exceptions

app = Flask(__name__)

PUBLIC_KEY = os.getenv("PUBLIC_KEY")


def verify_signature(req):
    signature = req.headers.get("X-Signature-Ed25519")
    timestamp = req.headers.get("X-Signature-Timestamp")

    if not signature or not timestamp:
        return False

    try:
        verify_key = nacl.signing.VerifyKey(bytes.fromhex(PUBLIC_KEY))

        verify_key.verify(
            timestamp.encode() + req.data,
            bytes.fromhex(signature)
        )

        return True

    except Exception:
        return False


@app.route("/", methods=["POST"])
def interactions():

    if not verify_signature(request):
        return "invalid request", 401

    data = request.json

    # Discord endpoint verification
    if data["type"] == 1:
        return jsonify({
            "type": 1
        })

    return jsonify({
        "type": 4,
        "data": {
            "content": "Hello from your app!"
        }
    })


@app.route("/", methods=["GET"])
def home():
    return "Discord Echo App is running"


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )
