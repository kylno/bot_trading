import csv
import os
import matplotlib.pyplot as plt
from collections import Counter

def generer_graphiques():
    chemin_logs = "data/logs.csv"
    if not os.path.exists(chemin_logs):
        print("❌ Aucune donnée à visualiser.")
        return

    with open(chemin_logs, "r", encoding="utf-8") as f:
        lignes = list(csv.reader(f))[1:]

    types = [ligne[1] for ligne in lignes if len(ligne) > 1]
    stats = Counter(types)

    plt.figure(figsize=(6, 4))
    plt.bar(stats.keys(), stats.values(), color="mediumseagreen")
    plt.title("Répartition des missions IA")
    plt.xlabel("Type")
    plt.ylabel("Quantité")
    plt.tight_layout()
    plt.savefig("exports/graphique_missions.png")
    plt.close()

    print("📊 Graphique généré : exports/graphique_missions.png")