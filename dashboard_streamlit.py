import streamlit as st
import requests
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=5000, key="refresh")  

st.set_page_config(page_title="Bot Trading Dashboard", layout="wide")

st.title("📊 Tableau de bord du Bot")

# Récupération des données depuis ton API Flask
try:
    config = requests.get("http://127.0.0.1:5000/").json()
    performance = requests.get("http://127.0.0.1:5000/performance").json()
    alerts = requests.get("http://127.0.0.1:5000/alerts").json()
except Exception as e:
    st.error(f"Erreur de connexion à l'API : {e}")
    st.stop()

# Affichage des données
st.subheader("⚙️ Configuration du Bot")
st.json(config)

st.subheader("📈 Performance")
col1, col2, col3 = st.columns(3)
col1.metric("Trades totaux", performance["total_trades"])
col2.metric("Win Rate", f"{performance['win_rate'] * 100:.1f}%")
col3.metric("Profit (€)", f"{performance['profit']:.2f}")

st.subheader("🚨 Alertes")
for alert in alerts:
    st.write(f"**{alert['symbol']}** → {alert['type'].upper()} (score: {alert['score']})")