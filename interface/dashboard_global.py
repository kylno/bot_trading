import streamlit as st
import json
import os

# 📦 Fonctions utilitaires
def charger_json(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}

def charger_jsonl(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return [json.loads(line) for line in f.readlines()]
    return []

# 🧠 Onglet 1 : Performances des bots
def vue_performance():
    st.header("📈 Performances des bots")
    perfs = charger_json("logs/performance_day.json")
    for bot, stats in perfs.items():
        st.subheader(f"🤖 {bot}")
        st.write(stats)

# 📡 Onglet 2 : Alertes scorées
def vue_alertes():
    st.header("📡 Alertes IA scorées")
    alertes = charger_json("logs/alertes_scored.json")
    for a in alertes:
        couleur = "🟢" if a["score"] >= 70 else "🟡" if a["score"] >= 40 else "🔴"
        st.markdown(f"{couleur} **{a['source']}** — {a['texte']}  \n🧠 Score : {a['score']}/100")

# 🧠 Onglet 3 : Recommandations IA
def vue_recommandations():
    st.header("🧠 Recommandations IA")
    recos = charger_json("logs/summary.json")
    for bot, reco in recos.items():
        st.subheader(f"🤖 {bot}")
        st.write(reco)

# 📜 Onglet 4 : Historique des décisions IA
def vue_historique():
    st.header("📜 Historique des recommandations")
    historique = charger_jsonl("logs/historique_reco.jsonl")
    for reco in historique[-20:][::-1]:  # Dernières 20
        st.markdown(f"🕒 {reco['timestamp']} — **{reco['bot']}** sur *{reco['actif']}*  \n🧠 Score : {reco['score']}  \n📌 Action : {reco['action_suggérée']}  \n🧾 Raison : {reco['raison']}")

# 🧭 Interface globale
st.set_page_config(page_title="Cockpit IA Global", layout="wide")
st.sidebar.title("🧭 Navigation cockpit IA")
choix = st.sidebar.radio("Choisir une vue :", ["📈 Performances", "📡 Alertes", "🧠 Recommandations", "📜 Historique"])

if choix == "📈 Performances":
    vue_performance()
elif choix == "📡 Alertes":
    vue_alertes()
elif choix == "🧠 Recommandations":
    vue_recommandations()
elif choix == "📜 Historique":
    vue_historique()