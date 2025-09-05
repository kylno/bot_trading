from flask import Flask, jsonify
from api import simulation_api, real_api
from config import USE_SIMULATION

app = Flask(__name__)

@app.route('/')
def index():
    data = simulation_api.get_bot_config() if USE_SIMULATION else real_api.get_bot_config()
    return jsonify(data)

@app.route('/performance')
def performance():
    data = simulation_api.get_performance() if USE_SIMULATION else real_api.get_performance()
    return jsonify(data)

@app.route('/alerts')
def alerts():
    data = simulation_api.get_alerts() if USE_SIMULATION else real_api.get_alerts()
    return jsonify(data)

if __name__ == '__main__':
    print("🚀 Serveur lancé sur http://127.0.0.1:5000")
    app.run(debug=True, port=5000)