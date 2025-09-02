import streamlit as st
from PIL import Image
import os

# Configuration de la page
st.set_page_config(page_title="Preview Visuel", layout="centered")

# Titre principal
st.title("🎨 Aperçu du Visuel")

# Chargement du fichier image
uploaded_file = st.file_uploader("📁 Importer une image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    # Ouverture de l'image
    image = Image.open(uploaded_file)

    # Options de personnalisation
    st.sidebar.header("🔧 Options")
    width = st.sidebar.slider("Largeur", 100, 1000, image.width)
    height = st.sidebar.slider("Hauteur", 100, 1000, image.height)
    grayscale = st.sidebar.checkbox("Niveaux de gris")

    # Transformation de l'image
    image_resized = image.resize((width, height))
    if grayscale:
        image_resized = image_resized.convert("L")

    # Affichage de l'image
    st.image(image_resized, caption="Aperçu du visuel", use_column_width=True)

    # Option de téléchargement
    st.download_button(
        label="📥 Télécharger l'image modifiée",
        data=image_resized.tobytes(),
        file_name="visuel_modifié.png",
        mime="image/png"
    )
else:
    st.info("Veuillez importer une image pour commencer.")