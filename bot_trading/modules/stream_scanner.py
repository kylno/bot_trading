# stream_scanner.py
import websocket
import json
import time
from datetime import datetime
import os

# === CONFIGURATION ===
TRACKED_SYMBOLS = ['btcusdt', 'ethusdt', 'solusdt', 'dogeusdt', 'linkusdt']
PUMP_WINDOW = 60  # secondes
THRESHOLD_PERCENT = 2.0  # Déclenche à +2 % en 60s
CONFIG_PATH = 'config_mode.json'

# === MODULES EXTERNES ===
try:
    from executor import executer_trade
except ImportError:
    def executer_trade(symbol, price, variation):
        print(f"[TEST] ➤ Trade fictif : {symbol.upper()} +{variation:.2f}%")

try:
    from alerte_discord import envoyer_alerte
except ImportError:
    def envoyer_alerte(symbol, variation):
        print(f"[TEST] ➤ Alerte Discord fictive : {symbol.upper()} +{variation:.2f}%")

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

# === LOGIQUE DE DÉTECTION DE PUMP ===
def detect_pump(symbol, price):
    now = time.time()

    if symbol not in price_memory:
        price_memory[symbol] = [(now, price)]
        return

    # Ajoute le nouveau point
    price_memory[symbol].append((now, price))
    # Garde les X dernières secondes
    price_memory[symbol] = [p for p in price_memory[symbol] if now - p[0] <= PUMP_WINDOW]

    old_time, old_price = price_memory[symbol][0]
    variation = ((price - old_price) / old_price) * 100

    if variation >= THRESHOLD_PERCENT:
        timestamp = datetime.fromtimestamp(now).strftime('%H:%M:%S')
        print(f"🚨 [{timestamp}] PUMP sur {symbol.upper()} ➤ +{variation:.2f}% en {PUMP_WINDOW}s")

        # Envoi de l’alerte Discord
        envoyer_alerte(symbol, variation)

        if lire_mode_auto():
            print("🤖 Mode AUTO ➤ trade simulé enclenché")
            executer_trade(symbol, price, variation)
        else:
            print("📣 Mode MANUEL ➤ observation uniquement")

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
    print("📡 Connexion WebSocket ➤", ', '.join([s.upper() for s in TRACKED_SYMBOLS]))

def on_error(ws, error):
    print("❌ Erreur WebSocket :", error)

def on_close(ws, code, msg):
    print("🔌 WebSocket fermé.")

# === LANCEMENT PRINCIPAL ===
if __name__ == "__main__":
    print("🧠 Lancement du scanner IA en temps réel...")
    ws = websocket.WebSocketApp(
        "wss://stream.binance.com:9443/ws",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close,
        on_open=on_open
    )
    ws.run_forever()