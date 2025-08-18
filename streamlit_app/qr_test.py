import streamlit as st
import qrcode
from PIL import Image
import io

st.set_page_config(page_title="📱 Test QR Code", layout="centered")
st.title("📱 Générateur de QR Code – Test module")

# 🔤 Donnée à encoder
texte = st.text_input("🔠 Texte à convertir en QR Code", value="https://copilot.microsoft.com")

# 📤 Génération du QR
if st.button("📸 Générer QR Code"):
    try:
        img = qrcode.make(texte)
        buf = io.BytesIO()
        img.save(buf)
        buf.seek(0)
        st.image(buf, caption="✅ QR Code généré", width=300)
    except Exception as e:
        st.error(f"❌ Erreur de génération : {e}")