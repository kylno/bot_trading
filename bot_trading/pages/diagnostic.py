import streamlit as st
import json
import os
import subprocess
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="📊 Diagnostic IA", layout="centered")
st.title("📊 État du cockpit IA – Diagnostic global")

# 🔁 Relancer le diagnostic
if st.button("🔁 Relancer auto_env_check"):
    try:
        subprocess.run(["python", "automation/auto_env_check.py"], check=True)
        st.success("✅ Diagnostic relancé")
    except Exception as e:
        st.error(f"❌ Erreur : {e}")

# 📥 Chargement des données
status_path = "logs/status_env.json"
log_file = "logs/config_log.txt"

if not os.path.exists(status_path):
    st.error("❌ Fichier `status_env.json` introuvable")
    st.stop()

with open(status_path, "r", encoding="utf-8") as f:
    status = json.load(f)

score = status.get("cockpit_score", 0)

# 🚦 Score cockpit IA + jauge
st.subheader("🚦 Score global du cockpit IA")
if score >= 90:
    st.success(f"🟢 Santé optimale ({score}%)")
elif score >= 70:
    st.warning(f"🟠 Santé moyenne ({score}%)")
else:
    st.error(f"🔴 Santé faible ({score}%)")
st.progress(score / 100)

# 🔴 Erreurs critiques détectées
erreurs = []
for mod, ok in status["modules"].items():
    if not ok: erreurs.append(f"Module KO : {mod}")
for api, ok in status["apis"].items():
    if not ok: erreurs.append(f"API KO : {api}")

nb_erreurs = len(erreurs)
if nb_erreurs > 0:
    st.error(f"❌ {nb_erreurs} erreur(s) critique(s) détectée(s)")
    for e in erreurs:
        st.markdown(f"- 🔴 {e}")
else:
    st.success("✅ Aucun module/API en panne")

# 📡 Latences API
st.subheader("⏱️ Latence réseau des APIs")
for api, latency in status.get("latence", {}).items():
    if latency is not None:
        st.write(f"📡 {api} : {latency}s")
    else:
        st.warning(f"📴 {api} : inaccessible")

# 📈 Historique du score cockpit IA
st.subheader("📈 Historique des scores cockpit IA")
if os.path.exists(log_file):
    dates, scores = [], []
    with open(log_file, "r", encoding="utf-8") as f:
        for line in f:
            if "Score :" in line:
                try:
                    date = line.split("]")[0].strip("[")
                    score_val = float(line.split("Score :")[1].split("%")[0].strip())
                    dates.append(date)
                    scores.append(score_val)
                except:
                    continue
    if scores:
        df = pd.DataFrame({"Date": dates, "Score": scores})
        fig, ax = plt.subplots()
        ax.plot(df["Date"], df["Score"], marker='o')
        ax.set_xticklabels(df["Date"], rotation=45, ha="right", fontsize=8)
        ax.set_ylabel("Score %")
        ax.set_title("📊 Évolution du cockpit IA")
        st.pyplot(fig)
    else:
        st.info("ℹ️ Aucun score enregistré")
else:
    st.warning("⚠️ Fichier `config_log.txt` introuvable")

# 📥 Téléchargement du rapport
with open(status_path, "rb") as f:
    st.download_button("📦 Télécharger le rapport complet", f, file_name="status_env.json")