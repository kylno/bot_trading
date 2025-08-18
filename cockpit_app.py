import streamlit as st
from PIL import Image

st.set_page_config(page_title="Cockpit IA", layout="wide")

st.markdown("## 🖼 Aperçu des animations cockpit IA")

# Chargement des images
check_img = Image.open("images/check.gif")
error_img = Image.open("images/error.gif")
rocket_img = Image.open("images/fusee.gif")
loading_img = Image.open("images/fond.gif")  # temporaire pour ⏳

# Affichage
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("### ✅ Validation système")
    st.image(check_img, caption="Check (validation système)", use_column_width=True)

with col2:
    st.markdown("### ❌ Panne détectée")
    st.image(error_img, caption="Error (panne détectée)", use_column_width=True)

with col3:
    st.markdown("### 🚀 Succès cockpit")
    st.image(rocket_img, caption="Fusée (succès cockpit)", use_column_width=True)

with col4:
    st.markdown("### ⏳ Attente")
    st.image(loading_img, caption="Loading (animation d'attente)", use_column_width=True)