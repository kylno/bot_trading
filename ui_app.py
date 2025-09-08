from flask import Flask, jsonify
from api.config import USE_SIMULATION
from api import real_api, simulation_api

app = Flask(__name__)

@app.route('/bot')
def bot():
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