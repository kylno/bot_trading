import pandas as pd
import os
import sys

# 🔧 Gère le chemin d'accès au dossier contenant 'utils_ia.py'
sys.path.append(os.path.abspath("streamlit_app"))

# 📥 Import de la fonction personnalisée
from ia_cerveaux.utils import charger_donnees

def analyse_tendance(df):
    if "prix" not in df.columns:
        raise ValueError("La colonne 'prix' est absente du DataFrame.")

    variation = df["prix"].pct_change().mean()

    if variation > 0.01:
        return "La tendance est à la hausse 📈"
    elif variation < -0.01:
        return "La tendance est à la baisse 📉"
    else:
        return "La tendance est stable ⚖️"

def main():
    chemin_donnees = "data/historique_trading.csv"

    try:
        df = charger_donnees(chemin_donnees)
        tendance = analyse_tendance(df)
        print(f"✅ Résultat de l'analyse : {tendance}")
    except Exception as e:
        print(f"❌ Erreur rencontrée : {e}")

if __name__ == "__main__":
    main()