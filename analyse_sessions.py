import os
import csv
from collections import defaultdict

# 📁 Dossier contenant les fichiers CSV
DOSSIER_LOGS = "logs"

def analyser_sessions(dossier=DOSSIER_LOGS):
    scores = defaultdict(list)

    # 🔍 Parcourir tous les fichiers de récapitulatif
    for fichier in os.listdir(dossier):
        if fichier.startswith("recap_trades") and fichier.endswith(".csv"):
            chemin = os.path.join(dossier, fichier)
            try:
                with open(chemin, "r", encoding="utf-8") as f:
                    reader = csv.DictReader(f)
                    for ligne in reader:
                        symbole = ligne["symbole"]
                        gain = float(ligne["gain_sécurisé"])
                        scores[symbole].append(gain)
            except Exception as e:
                print(f"⚠️ Erreur lecture {fichier} : {e}")

    # 🧮 Calcul des moyennes
    tableau = []
    for symbole, gains in scores.items():
        total = sum(gains)
        moyenne = total / len(gains)
        tableau.append({
            "symbole": symbole,
            "sessions": len(gains),
            "gain_total": round(total, 2),
            "gain_moyen": round(moyenne, 2)
        })

    # 📋 Affichage du tableau comparatif
    print("\n🏆 Comparatif des performances par symbole :")
    print(f"{'Symbole':<10} {'Sessions':<10} {'Total (€)':<12} {'Moyenne (€)':<12}")
    print("-" * 45)
    for ligne in sorted(tableau, key=lambda x: x["gain_moyen"], reverse=True):
        print(f"{ligne['symbole']:<10} {ligne['sessions']:<10} {ligne['gain_total']:<12} {ligne['gain_moyen']:<12}")

if __name__ == "__main__":
    analyser_sessions()
    
    import plotly.graph_objects as go
from datetime import datetime

def afficher_graphique_comparatif(tableau):
    symboles = [ligne["symbole"] for ligne in tableau]
    moyennes = [ligne["gain_moyen"] for ligne in tableau]

    fig = go.Figure(data=[
        go.Bar(x=symboles, y=moyennes, marker_color='royalblue')
    ])
    fig.update_layout(
        title="📊 Moyenne des gains sécurisés par symbole",
        xaxis_title="Symbole",
        yaxis_title="Gain moyen (€)",
        template="plotly_white"
    )

    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_fichier = f"logs/graphique_comparatif_{horodatage}.html"
    fig.write_html(nom_fichier)
    print(f"✅ Graphique interactif enregistré : {nom_fichier}")
    afficher_graphique_comparatif(tableau)