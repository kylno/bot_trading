import streamlit as st
import json
import os

st.set_page_config(page_title="⚠️ Erreurs cockpit IA", layout="centered")
st.title("⚠️ Pannes et anomalies détectées")

status_path = "logs/status_env.json"

if not os.path.exists(status_path):
    st.error("❌ Fichier de diagnostic manquant")
    st.stop()

with open(status_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Modules en erreur
st.subheader("🔧 Modules en erreur")
error_modules = [name for name, status in data.get("modules", {}).items() if not status]
if error_modules:
    for module in error_modules:
        st.error(f"❌ Module défectueux : {module}")
else:
    st.success("✅ Aucun module défectueux")

# APIs non connectées
st.subheader("🌐 APIs non connectées")
error_apis = [name for name, status in data.get("apis", {}).items() if not status]
if error_apis:
    for api in error_apis:
        st.warning(f"📴 API non disponible : {api}")
else:
    st.success("✅ Toutes les APIs répondent")

# État global du système
st.subheader("📊 État global du cockpit IA")
if not error_modules and not error_apis:
    if os.path.exists("streamlit_app/images/check.gif"):
        st.image("streamlit_app/images/check.gif", caption="🧠 Système stable")
    else:
        st.success("🧠 Système stable — tous les voyants sont au vert")
else:
    if os.path.exists("streamlit_app/images/error.gif"):
        st.image("streamlit_app/images/error.gif", caption="❗ Problèmes détectés")
    else:
        st.error("❗ Problèmes détectés dans le cockpit IA")