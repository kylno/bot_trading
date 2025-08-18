# dashboard_ia.py
import streamlit as st
from ia_cerveaux.utils_ia import charger_donnees, apercu_donnees
from evaluateur import run as evaluer
from predicateur import run as predire

st.set_page_config(page_title="Dashboard IA", layout="wide")
st.title("🤖 Tableau de bord - IA Trading")

# Chargement des données
df = charger_donnees("data/historique_trading.csv")
if df is not None:
    apercu_donnees(df)

# Boutons d'action
if st.button("📈 Analyser tendance"):
    predire()

if st.button("🧪 Évaluer IA"):
    evaluer()