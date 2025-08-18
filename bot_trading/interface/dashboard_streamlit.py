import streamlit as st
import json
import os
import subprocess
from datetime import datetime

# Chemins
CONFIG_PATH = "config/bot_config.json"
LOG_PATH = "logs/trades.log"
PERF_VIEW = {
    "Jour": "logs/performance_day.json",
    "Semaine": "logs/performance_week.json",
    "Mois": "logs/performance_month.json"
}

# Chargement JSON
def charger_json(path):
    if not os.path.isfile(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)

# Fiche bot
def afficher_fiche(nom, infos):
    st.subheader(f"📘 Fiche : {nom}")
    for cle, val in infos.items():
        if isinstance(val, list):
            st.markdown(f"**{cle.replace('_', ' ').capitalize()}**:")
            for item in val:
                st.markdown(f"• {item}")
        else:
            st.markdown(f"**{cle.replace('_', ' ').capitalize()}**: {val}")

# Répartition du capital
def afficher_allocation(bots):
    st.subheader("💰 Répartition du capital")
    alloc = {k: int(v.get("capital_allocation", 0)*100) for k,v in bots.items()}
    st.bar_chart(alloc)

# Courbes de perf
def afficher_perf_temporelle(data, vue):
    st.subheader(f"📈 Performance par bot ({vue})")
    for bot, perf in data.items():
        st.markdown(f"**📊 {bot}**")
        st.line_chart(perf)

# Vue combinée
def afficher_vue_combinée(data):
    st.subheader("🧠 Vue combinée — Stats globales")
    stats = {}
    for bot, perf in data.items():
        if perf:
            moy = round(sum(perf.values()) / len(perf), 2)
            stats[bot] = {
                "📈 Moyenne %": moy,
                "🏆 Max %": max(perf.values()),
                "⚠️ Drawdown %": min(perf.values())
            }
    for bot, infos in stats.items():
        st.markdown(f"**🧬 {bot}**")
        st.write(infos)

# Synthèse IA
def générer_synthèse(data):
    if not data:
        return "📭 Aucune donnée disponible."
    résumé = []
    for bot, perf in data.items():
        if not perf:
            continue
        moyenne = round(sum(perf.values()) / len(perf), 2)
        tendance = "📈 progresse bien" if moyenne > 0 else "📉 en retrait"
        résumé.append(f"{bot} {tendance} avec une moyenne de {moyenne}%.")
    return "\n".join(résumé)

# Suggestions IA
def decisions_strategiques(data):
    suggestions = []
    for bot, perf in data.items():
        vals = list(perf.values())
        if not vals:
            continue
        avg = sum(vals)/len(vals)
        worst = min(vals)
        if avg > 15:
            suggestions.append(f"🔼 **{bot}** surperforme — envisage d’augmenter le capital ou d’élargir le scope.")
        elif worst < -10:
            suggestions.append(f"⚠️ **{bot}** subit des pertes — réduire le risque ou revoir la stratégie.")
        elif avg < 2:
            suggestions.append(f"🧊 **{bot}** est neutre — pause recommandée ou mise à niveau.")
    return suggestions

# Logs
def charger_logs(path=LOG_PATH, n=10):
    if not os.path.isfile(path):
        return ["📭 Aucun log."]
    with open(path, encoding="utf-8") as f:
        return [l.strip() for l in f.readlines()[-n:]]

def afficher_logs(logs):
    st.subheader("📁 Derniers trades")
    for l in logs:
        st.text(l)

# 🧠 Interface principale
def main():
    st.set_page_config(page_title="Cockpit IA", layout="centered")
    st.title("🧠 Centre de Commandement Bots IA")

    # Chargement config
    bots = charger_json(CONFIG_PATH)
    if not bots:
        st.warning("📭 Aucun bot trouvé dans la config.")
        return

    noms_bots = list(bots.keys())
    selection = st.selectbox("🎯 Sélectionne un bot", noms_bots)
    afficher_fiche(selection, bots[selection])

    st.markdown("---")
    afficher_allocation(bots)

    # 🔄 Bouton actualisation
    if st.button("🔄 Actualiser les performances"):
        result = subprocess.run(["python", "utils/group_perf.py"], capture_output=True, text=True)
        if result.returncode == 0:
            st.success("📊 Performances mises à jour.")
        else:
            st.error("❌ Erreur de mise à jour.")
            st.text(result.stderr)

    # 📈 Vue temporelle
    st.markdown("---")
    vue = st.selectbox("🕒 Vue temporelle :", list(PERF_VIEW.keys()))
    perf_data = charger_json(PERF_VIEW[vue])

    if perf_data:
        afficher_perf_temporelle(perf_data, vue)
        st.markdown("---")
        afficher_vue_combinée(perf_data)
        st.markdown("---")
        st.subheader("🧠 Synthèse IA des performances")
        st.markdown(générer_synthèse(perf_data))
        st.markdown("---")
        st.subheader("🪞 Suggestions IA — Stratégies")
        for s in decisions_strategiques(perf_data):
            st.markdown(s)
    else:
        st.info("📭 Aucune performance chargée.")

    st.markdown("---")
    logs = charger_logs()
    afficher_logs(logs)

    st.markdown("---")
    st.caption("🔧 Cockpit IA Streamlit — Piloté par Kylian 🚀")

if __name__ == "__main__":
    main()