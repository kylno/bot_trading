import pandas as pd
import matplotlib.pyplot as plt
import os

def generer_camembert_repartition():
    chemin_csv = "log/fourmi_log.csv"
    if not os.path.exists(chemin_csv):
        print("❌ Fichier CSV introuvable.")
        return

    df = pd.read_csv(chemin_csv)

    if "Fourmi" not in df.columns:
        print("❌ Colonne 'Fourmi' introuvable dans le fichier CSV.")
        return

    repartition = df["Fourmi"].value_counts()

    couleurs = plt.cm.Pastel1.colors
    plt.figure(figsize=(6, 6))
    plt.pie(repartition, labels=repartition.index, autopct="%1.1f%%", startangle=140, colors=couleurs)
    plt.title("Répartition des exécutions par Fourmi", fontsize=14)
    plt.axis("equal")

    os.makedirs("exports", exist_ok=True)
    chemin_image = "exports/graphique_missions.png"
    plt.savefig(chemin_image, bbox_inches="tight")
    plt.close()

    print(f"🖼️ Graphique généré : {chemin_image}")

if __name__ == "__main__":
    generer_camembert_repartition()