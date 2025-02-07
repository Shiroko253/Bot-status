from flask import Flask, request, jsonify

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
    bot_status = request.json
    return jsonify({"message": "Status updated"}), 200

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(bot_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
