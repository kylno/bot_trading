import streamlit as st
from PIL import Image

# Configuration de la page
st.set_page_config(page_title="Cockpit IA", layout="wide")

# Titre principal
st.markdown("<h1 style='text-align: center; color: white;'>Aperçu visuel du cockpit IA</h1>", unsafe_allow_html=True)

# Espacement
st.markdown("##")

# Création des colonnes
col1, col2, col3 = st.columns(3)

# ✅ Validation système
with col1:
    st.markdown("<h3 style='text-align: center; color: white;'>Validation système</h3>", unsafe_allow_html=True)
    st.image("assets/validation.png", use_container_width=True)

# ❌ Erreur détectée
with col2:
    st.markdown("<h3 style='text-align: center; color: white;'>Erreur détectée</h3>", unsafe_allow_html=True)
    st.image("assets/erreur.png", use_container_width=True)

# 🚀 Décollage cockpit
with col3:
    st.markdown("<h3 style='text-align: center; color: white;'>Décollage cockpit</h3>", unsafe_allow_html=True)
    st.image("assets/rocket.png", use_container_width=True)

# Optionnel : bouton de déploiement
st.markdown("<div style='text-align: right;'><button style='padding:10px 20px;'>Déployer</button></div>", unsafe_allow_html=True)