from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

STATUS_FILE = "bot_status.json"

bot_status = {
    "bot_online": False,
    "server_count": 0,
    "ping": 0
}

def load_status():
    global bot_status
    if os.path.exists(STATUS_FILE):
        with open(STATUS_FILE, "r") as f:
            bot_status = json.load(f)

def save_status():
    with open(STATUS_FILE, "w") as f:
        json.dump(bot_status, f)

load_status()

@app.route("/update_status", methods=["POST"])
def update_status():
    global bot_status
    data = request.get_json()
    if not data or not all(k in data for k in ["bot_online", "server_count", "ping"]):
        return jsonify({"error": "Invalid request"}), 400
    bot_status = data
    save_status()
    return jsonify({"message": "Status updated"}), 200

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(bot_status)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
