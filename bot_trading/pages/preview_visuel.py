import streamlit as st
import os

st.set_page_config(page_title="🎨 Aperçu des visuels", layout="centered")
st.title("🎨 Aperçu des animations cockpit IA")

image_paths = {
    "✅ Check (validation système)": "images/check.gif",
    "❌ Error (panne détectée)": "images/error.gif",
    "🚀 Fusée (succès cockpit)": "images/fusee.gif",
    "⏳ Loading (animation d’attente)": "images/loading.gif"
}

for label, path in image_paths.items():
    st.markdown(f"### {label}")
    if os.path.exists(f"../{path}"):
        st.image(f"../{path}", width=200)
    else:
        st.error(f"⚠️ Fichier manquant : `{path}`")