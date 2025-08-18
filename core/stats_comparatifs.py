import json
import os

# 📦 Fichiers de performances
FILES = {
    "Jour": "logs/performance_day.json",
    "Semaine": "logs/performance_week.json",
    "Mois": "logs/performance_month.json"
}

def charger_perfs(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}

def comparer_bots():
    tableau = {}

    for période, fichier in FILES.items():
        perfs = charger_perfs(fichier)
        for bot, stats in perfs.items():
            if bot not in tableau:
                tableau[bot] = {}
            tableau[bot][période] = stats.get("performance", 0)

    return tableau

# 🚀 Affichage console
if __name__ == "__main__":
    tableau = comparer_bots()
    print("📊 Comparatif des performances IA")
    print("-" * 40)
    for bot, stats in tableau.items():
        print(f"🤖 {bot}")
        for période, perf in stats.items():
            print(f"  {période} : {perf:.2f}%")
        print("-" * 40)