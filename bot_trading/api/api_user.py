from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route("/performance")
def get_performance():
    with open("logs/performance_month.json", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/alertes")
def get_alertes():
    with open("logs/alertes_scored.json", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

@app.route("/bots")
def get_bots():
    with open("config/bot_config.json", encoding="utf-8") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)