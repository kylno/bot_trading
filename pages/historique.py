import streamlit as st
import os

st.set_page_config(page_title="📜 Historique cockpit IA", layout="centered")
st.title("📜 Historique des activités cockpit IA")

# 🧠 Historique de config IA
st.subheader("📝 Sauvegardes de configuration")

log_config_path = "logs/config_log.txt"
if os.path.exists(log_config_path):
    with open(log_config_path, "r", encoding="utf-8") as f:
        lines = f.readlines()[-10:]
    for line in lines[::-1]:
        st.markdown(f"🧠 {line.strip()}")
else:
    st.info("📂 Aucun historique de configuration enregistré")

# 🧳 Historique des exports cockpit
st.subheader("🗂️ Exports de valise IA")

export_log_path = "logs/exports_log.txt"
if os.path.exists(export_log_path):
    with open(export_log_path, "r", encoding="utf-8") as f:
        lines = f.readlines()[-10:]
    for line in lines[::-1]:
        st.markdown(f"📦 {line.strip()}")
else:
    st.info("📂 Aucun export enregistré pour le moment")