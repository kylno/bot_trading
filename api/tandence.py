import json
import os
from collections import defaultdict

# 📦 Fichier d'alertes scorées
ALERTES_PATH = "logs/alertes_scored.json"

# 🧠 Mots-clés haussiers / baissiers
HAUSSIER = ["pump", "breakout", "bullish", "buy signal", "explose"]
BAISSIER = ["crash", "bearish", "sell signal", "liquidation", "drawdown"]

def charger_alertes():
    if os.path.exists(ALERTES_PATH):
        with open(ALERTES_PATH, encoding="utf-8") as f:
            return json.load(f)
    return []

def analyser_tendance(alertes):
    tendances = defaultdict(lambda: {"haussier": 0, "baissier": 0})

    for a in alertes:
        texte = a["texte"].lower()
        actif = "inconnu"

        # Détection de l'actif mentionné
        for mot in ["bitcoin", "eth", "solana", "apple", "nasdaq", "gold"]:
            if mot in texte:
                actif = mot

        # Comptage des mots-clés
        if any(k in texte for k in HAUSSIER):
            tendances[actif]["haussier"] += 1
        if any(k in texte for k in BAISSIER):
            tendances[actif]["baissier"] += 1

    # Déduction de la tendance
    resultats = {}
    for actif, scores in tendances.items():
        h, b = scores["haussier"], scores["baissier"]
        if h > b:
            resultats[actif] = "🔼 Haussière"
        elif b > h:
            resultats[actif] = "🔽 Baissière"
        else:
            resultats[actif] = "⏸️ Neutre"

    return resultats

# 🚀 Exemple d'utilisation
if __name__ == "__main__":
    alertes = charger_alertes()
    tendances = analyser_tendance(alertes)
    print("📊 Tendances détectées :")
    for actif, tendance in tendances.items():
        print(f"🧠 {actif.capitalize()} → {tendance}")