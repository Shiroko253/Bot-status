from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 存儲 bot 狀態
bot_status = {
    "bot_online": False,
    "server_count": 0,
    "ping": 0
}

@app.route("/update_status", methods=["POST"])
def update_status():
    global bot_status
    data = request.get_json()
    if not data or not all(k in data for k in ["bot_online", "server_count", "ping"]):
        return jsonify({"error": "Invalid request"}), 400
    bot_status = data
    return jsonify({"message": "Status updated"}), 200

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(bot_status)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
