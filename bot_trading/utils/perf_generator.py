import os
import json
import re

LOG_FILE = "logs/trades.log"
OUTPUT_FILE = "logs/performance.json"

def extraire_performances(n=30):
    if not os.path.isfile(LOG_FILE):
        print("❌ Fichier de log introuvable.")
        return {}

    perf = {}

    with open(LOG_FILE, encoding="utf-8") as f:
        lignes = f.readlines()[-n:]  # Les n derniers trades

    for ligne in lignes:
        match = re.match(r"\[(.+?)\]\s*([+-]?[0-9.]+)%", ligne.strip())
        if match:
            bot, val = match.groups()
            val = float(val)
            if bot not in perf:
                perf[bot] = []
            perf[bot].append(val)

    return perf

def sauvegarder_performance(data):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Performances enregistrées dans '{OUTPUT_FILE}'.")

if __name__ == "__main__":
    data = extraire_performances()
    sauvegarder_performance(data)