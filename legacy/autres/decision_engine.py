import json
import os
from datetime import datetime, timedelta
from stream_scanner import executer_trade

EVENTS_PATH = "events.json"
DECISIONS_PATH = "decisions.json"
FENETRE_ANALYSE = 20  # nombre d'événements récents à analyser
DELAI_RETRADE = timedelta(minutes=30)  # délai minimum entre deux trades sur le même symbole

def charger_evenements():
    if not os.path.exists(EVENTS_PATH):
        return []
    with open(EVENTS_PATH, "r") as f:
        return json.load(f)

def charger_decisions():
    if not os.path.exists(DECISIONS_PATH):
        return []
    with open(DECISIONS_PATH, "r") as f:
        return json.load(f)

def enregistrer_decision(symbol, price, variation):
    decision = {
        "symbol": symbol,
        "price": price,
        "variation": variation,
        "timestamp": datetime.now().isoformat()
    }
    decisions = charger_decisions()
    decisions.append(decision)
    with open(DECISIONS_PATH, "w") as f:
        json.dump(decisions, f, indent=2)

def dernier_trade(symbol):
    decisions = charger_decisions()
    for d in reversed(decisions):
        if d["symbol"] == symbol:
            return datetime.fromisoformat(d["timestamp"])
    return None

def calculer_seuil_adaptatif(data):
    recent = data[-FENETRE_ANALYSE:]
    variations = [e["variation"] for e in recent]
    if not variations:
        return 50  # seuil par défaut
    moyenne = sum(variations) / len(variations)
    return max(10, moyenne * 2)  # seuil dynamique

def calculer_scores(data):
    scores = {}
    for event in data[-FENETRE_ANALYSE:]:
        symbol = event["symbol"]
        variation = event["variation"]
        scores.setdefault(symbol, 0)
        scores[symbol] += variation
    return scores

def prendre_decision():
    data = charger_evenements()
    if not data:
        return

    seuil = calculer_seuil_adaptatif(data)
    scores = calculer_scores(data)

    for symbol, score in scores.items():
        last_trade_time = dernier_trade(symbol)
        if last_trade_time and datetime.now() - last_trade_time < DELAI_RETRADE:
            continue  # skip si déjà tradé récemment

        if score >= seuil:
            dernier_event = [e for e in reversed(data) if e["symbol"] == symbol][0]
            print(f"🧠 IA ➤ Trade sur {symbol.upper()} (score={score:.2f}, seuil={seuil:.2f})")
            executer_trade(symbol, dernier_event["price"], dernier_event["variation"])
            enregistrer_decision(symbol, dernier_event["price"], dernier_event["variation"])

if __name__ == "__main__":
    prendre_decision()