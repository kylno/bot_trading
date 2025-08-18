# main.py
import streamlit as st
import os
from utils import afficher_gif

# main.py

import streamlit as st
from streamlit_app.preview_visuel import afficher_cockpit

afficher_cockpit()

st.set_page_config(page_title="Centre de Lancement", layout="centered")

st.title("🚀 Cockpit de Décollage")
st.markdown("Bienvenue dans le centre de lancement. Prépare-toi au décollage !")

# Vérification du fichier
gif_path = "images/fusee.gif"
st.write("📂 Répertoire courant :", os.getcwd())
st.write("🧠 Fichier trouvé :", os.path.exists(gif_path))

# Bouton d'action
if st.button("Lancer la mission 🚀"):
    afficher_gif(gif_path, "Décollage en cours...")
else:
    st.info("💡 Appuie sur le bouton pour lancer la fusée.")