import streamlit as st
import json

def charger_alertes_scored(fichier="logs/alertes_scored.json"):
    try:
        with open(fichier, encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

def afficher_tableau_alertes(data):
    st.title("📡 Radar IA — Alertes scorées")
    for a in data:
        score = a.get("score", 0)
        couleur = "🟢" if score >= 70 else "🟡" if score >= 40 else "🔴"
        st.markdown(f"{couleur} **{a['source']}** — {a['texte']}  \n🧠 Score : {score}/100")

if __name__ == "__main__":
    data = charger_alertes_scored()
    afficher_tableau_alertes(data)