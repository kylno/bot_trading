import websocket
import json
import time
from datetime import datetime
import os
import logging
import random
import sys

# === CONFIGURATION ===
TRACKED_SYMBOLS = ['btcusdt', 'ethusdt', 'solusdt', 'dogeusdt', 'linkusdt']
PUMP_WINDOW = 60  # secondes
THRESHOLD_PERCENT = 2.0
CONFIG_PATH = 'config_mode.json'
EVENTS_PATH = 'events.json'
PRICE_PATH = 'price.json'

# === LOGGING ===
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# === MODULES EXTERNES ===
try:
    from executor import executer_trade
except ImportError:
    def executer_trade(symbol, price, variation):
        logging.info(f"[TEST] ➤ Trade fictif : {symbol.upper()} +{variation:.2f}%")

try:
    from alerte_discord import envoyer_alerte
except ImportError:
    def envoyer_alerte(symbol, variation):
        logging.info(f"[TEST] ➤ Alerte Discord fictive : {symbol.upper()} +{variation:.2f}%")

# === MÉMOIRE DES PRIX ===
price_memory = {}

# === UTILITAIRE : lecture du mode auto
def lire_mode_auto():
    if not os.path.exists(CONFIG_PATH):
        return False
    try:
        with open(CONFIG_PATH, 'r') as f:
            config = json.load(f)
            return config.get("auto_mode", False)
    except:
        return False

# === SAUVEGARDE DES ÉVÉNEMENTS ===
def enregistrer_evenement(symbol, price, variation):
    event = {
        "symbol": symbol,
        "price": price,
        "variation": variation,
        "timestamp": datetime.now().isoformat()
    }
    try:
        if os.path.exists(EVENTS_PATH):
            with open(EVENTS_PATH, "r") as f:
                data = json.load(f)
        else:
            data = []
        data.append(event)
        with open(EVENTS_PATH, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        logging.error(f"Erreur enregistrement événement : {e}")

# === SAUVEGARDE DU PRIX ACTUEL ===
def enregistrer_prix(symbol, price):
    try:
        if os.path.exists(PRICE_PATH):
            with open(PRICE_PATH, "r") as f:
                data = json.load(f)
        else:
            data = {}
        data[symbol] = price
        with open(PRICE_PATH, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        logging.error(f"Erreur enregistrement prix : {e}")

# === LOGIQUE DE DÉTECTION DE PUMP ===
def detect_pump(symbol, price):
    now = time.time()
    enregistrer_prix(symbol, price)

    if symbol not in price_memory:
        price_memory[symbol] = [(now, price)]
        return

    price_memory[symbol].append((now, price))
    price_memory[symbol] = [p for p in price_memory[symbol] if now - p[0] <= PUMP_WINDOW]

    old_time, old_price = price_memory[symbol][0]
    variation = ((price - old_price) / old_price) * 100

    if variation >= THRESHOLD_PERCENT:
        timestamp = datetime.fromtimestamp(now).strftime('%H:%M:%S')
        logging.info(f"🚨 [{timestamp}] PUMP sur {symbol.upper()} ➤ +{variation:.2f}% en {PUMP_WINDOW}s")

        envoyer_alerte(symbol, variation)
        enregistrer_evenement(symbol, price, variation)

        if lire_mode_auto():
            logging.info("🤖 Mode AUTO ➤ trade simulé enclenché")
            executer_trade(symbol, price, variation)
        else:
            logging.info("📣 Mode MANUEL ➤ observation uniquement")

# === WEBSOCKET HANDLERS ===
def on_message(ws, message):
    data = json.loads(message)
    if 's' in data and 'c' in data:
        symbol = data['s'].lower()
        price = float(data['c'])
        detect_pump(symbol, price)

def on_open(ws):
    params = [f"{symbol}@ticker" for symbol in TRACKED_SYMBOLS]
    payload = {
        "method": "SUBSCRIBE",
        "params": params,
        "id": 1
    }
    ws.send(json.dumps(payload))
    logging.info("📡 Connexion WebSocket ➤ " + ', '.join([s.upper() for s in TRACKED_SYMBOLS]))

def on_error(ws, error):
    logging.error("❌ Erreur WebSocket : " + str(error))

def on_close(ws, code, msg):
    logging.warning("🔌 WebSocket fermé.")

# === MODE TEST LOCAL ===
def mode_test():
    logging.info("🧪 Mode TEST local activé")
    while True:
        for symbol in TRACKED_SYMBOLS:
            price = random.uniform(100, 200)
            detect_pump(symbol, price)
        time.sleep(1)

# === LANCEMENT PRINCIPAL ===
if __name__ == "__main__":
    logging.info("🧠 Lancement du scanner IA en temps réel...")

    if "--test" in sys.argv:
        mode_test()
    else:
        ws = websocket.WebSocketApp(
            "wss://stream.binance.com:9443/ws",
            on_message=on_message,
            on_error=on_error,
            on_close=on_close,
            on_open=on_open
        )
        ws.run_forever(ping_interval=30, ping_timeout=10)