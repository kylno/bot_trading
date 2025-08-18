import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath("streamlit_app"))

from ia_cerveaux.profiteur import Profiteur
from ia_cerveaux.strategiste_fantome import StrategisteFantome
from ia_cerveaux.diagnostiqueur import Diagnostiqueur

# 🔽 Chargement des données
def charger_donnees(path):
    try:
        return pd.read_csv(path)
    except Exception:
        st.error("Impossible de charger les données.")
        return None

# 🔁 Analyse de tendance
def analyse_tendance(df, seuil=0.01):
    variation = df["prix"].pct_change().mean()
    if variation > seuil:
        return "hausse"
    elif variation < -seuil:
        return "baisse"
    else:
        return "neutre"

# 🧠 Sélection du cerveau IA
def obtenir_conseil(tendance, cerveau):
    return cerveau.conseiller()

# 🎨 Interface Streamlit
st.title("🧠 Tableau de bord IA Trading")
st.markdown("Analyse de tendance et conseils automatisés")

fichier = st.text_input("Chemin vers le fichier CSV", "data/historique_trading.csv")

df = charger_donnees(fichier)
if df is not None:
    st.line_chart(df["prix"])

    tendance = analyse_tendance(df)
    st.info(f"Tendance détectée : **{tendance.upper()}**")

    # 🧠 Choix du cerveau IA
    choix = st.selectbox("Choisissez votre cerveau IA", [
        "Profiteur", "Diagnostiqueur", "StrategisteFantome"
    ])

    if choix == "Profiteur":
        bot = Profiteur()
    elif choix == "Diagnostiqueur":
        bot = Diagnostiqueur()
    else:
        bot = StrategisteFantome()

    conseil = obtenir_conseil(tendance, bot)
    st.success(f"💡 Conseil de {choix} : {conseil}")