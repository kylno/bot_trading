# graph_profit.py

import matplotlib.pyplot as plt
import csv
from datetime import datetime
import os

def generer_graphe_performance():
    dates = []
    capital_evolution = []
    capital = 1000.0  # capital initial

    try:
        with open("data/profit_log.csv", "r") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 5:
                    date_str = f"{row[0]} {row[1]}"
                    try:
                        moment = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
                    except:
                        continue
                    profit = float(row[4])
                    capital += profit
                    dates.append(moment)
                    capital_evolution.append(round(capital, 2))
    except Exception as e:
        print(f"❌ Erreur lecture CSV : {e}")
        return

    if not dates:
        print("⚠️ Aucun trade trouvé dans profit_log.csv")
        return

    # 📈 Création du graphe
    plt.figure(figsize=(10, 5))
    plt.plot(dates, capital_evolution, marker='o', linestyle='-', color='blue')
    plt.title("Évolution du capital IA 📈")
    plt.xlabel("Date")
    plt.ylabel("Capital (USDT)")
    plt.grid(True)
    plt.tight_layout()

    # 📦 Sauvegarde dans static/
    output_path = os.path.join("static", "capital_graph.png")
    try:
        plt.savefig(output_path)
        print(f"✅ Graphe généré : {output_path}")
    except Exception as e:
        print(f"❌ Erreur lors de la sauvegarde du graphe : {e}")
        if __name__ == "__main__":
          generer_graphe_performance()
    print("📊 Graphe généré ou message affiché.")