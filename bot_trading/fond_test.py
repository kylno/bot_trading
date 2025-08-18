import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")
st.title("🌌 Test visuel du fond cockpit IA")

image_path = "streamlit_app/assets/fond.gif"  # ← adapte le nom si besoin
st.image(Image.open(image_path), use_container_width=True)