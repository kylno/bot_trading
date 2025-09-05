# 📦 Imports
import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# 🔁 Rafraîchissement automatique
st_autorefresh(interval=5000, key="refresh")

# ⚙️ Configuration de la page
st.set_page_config(page_title="Bot Trading Dashboard", layout="wide")
st.title("📈 Tableau de bord du Bot")

# 📡 Récupération des données depuis Flask
try:
    config = requests.get("http://127.0.0.1:5000/config").json()
    performance = requests.get("http://127.0.0.1:5000/performance").json()
    alerts = requests.get("http://127.0.0.1:5000/alerts").json()
except Exception as e:
    st.error(f"❌ Erreur de connexion à l'API : {e}")
    st.stop()

# ✅ État du bot
if config["is_running"]:
    st.success("✅ En cours d'exécution")
else:
    st.error("❌ Bot non actif")

# ⚙️ Configuration du bot
st.subheader("⚙️ Configuration du Bot")
st.json(config)

# 📊 Performance
st.subheader("📊 Performance")
col1, col2, col3 = st.columns(3)
col1.metric("Trades", performance["total_trades"])
col2.metric("Profit (€)", performance["profit"])
col3.metric("Win Rate", f"{performance['win_rate'] * 100:.1f}%")

objectif = 3000
progress = min(performance["profit"] / objectif, 1.0)
st.progress(progress)
st.caption(f"Objectif : {objectif} €")

# 🚨 Alertes
st.subheader("🚨 Alertes")
for alert in alerts:
    score = alert["score"]
    color = "🟢" if score > 80 else "🟡" if score > 50 else "🔴"
    st.write(f"{color} {alert['symbol']} - {alert['type'].upper()} (Score: {score})")

# 📆 Sessions de trading
st.subheader("📆 Sessions de trading")
try:
    sessions_df = pd.read_csv("data/log_data_cleaned_v2.csv")
    st.dataframe(sessions_df.style.format({"profit": "{:.2f} €"}).background_gradient(cmap="Blues"))
except Exception:
    st.info("Aucune session disponible.")

# 📜 Historique des trades
st.subheader("📄 Historique des trades")
if "sessions_df" in locals():
    for _, row in sessions_df.iterrows():
        icon = "🟢" if row["profit_percent"] > 0 else "🔴"
        st.write(f"{icon} {row['symbol']} - {row['type'].upper()} : {row['profit_percent']}%")

# 📲 Bouton Telegram
if st.button("📲 Envoyer une alerte Telegram"):
    response = requests.post("http://127.0.0.1:5000/send_alert")
    if response.status_code == 200:
        st.success("Alerte envoyée avec succès !")
    else:
        st.error("Échec de l’envoi.")