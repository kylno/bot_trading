import os
import json
import re
from collections import defaultdict
from datetime import datetime

LOG_PATH = "logs/trades.log"
OUT_DAY = "logs/performance_day.json"
OUT_WEEK = "logs/performance_week.json"
OUT_MONTH = "logs/performance_month.json"

def lire_trades(log_path=LOG_PATH):
    if not os.path.isfile(log_path):
        print("❌ Fichier introuvable :", log_path)
        return []

    with open(log_path, encoding="utf-8") as f:
        lignes = f.readlines()

    trades = []
    for ligne in lignes:
        match = re.match(r"(\d{4}-\d{2}-\d{2})\s+\[(.+?)\]\s+([+-]?[0-9.]+)%", ligne.strip())
        if match:
            date_str, bot, perf_str = match.groups()
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d")
                perf = float(perf_str)
                trades.append((bot, date, perf))
            except ValueError:
                continue
    return trades

def regrouper_par_periode(trades, mode="day"):
    data = defaultdict(lambda: defaultdict(list))

    for bot, date, perf in trades:
        if mode == "day":
            key = date.strftime("%Y-%m-%d")
        elif mode == "week":
            key = date.strftime("%Y-W%U")
        elif mode == "month":
            key = date.strftime("%Y-%m")
        else:
            continue

        data[bot][key].append(perf)

    return data

def calculer_moyennes(data):
    moyennes = {}
    for bot, periodes in data.items():
        moyennes[bot] = {periode: round(sum(vals)/len(vals), 2) for periode, vals in periodes.items()}
    return moyennes

def enregistrer(data, chemin):
    with open(chemin, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"✅ Sauvegardé : {chemin}")

def main():
    trades = lire_trades()

    if not trades:
        print("📭 Aucun trade à analyser.")
        return

    for mode, chemin in [("day", OUT_DAY), ("week", OUT_WEEK), ("month", OUT_MONTH)]:
        regroupés = regrouper_par_periode(trades, mode)
        moyennes = calculer_moyennes(regroupés)
        enregistrer(moyennes, chemin)

if __name__ == "__main__":
    main()