import streamlit as st
import os
import zipfile
import json
import requests
import smtplib
from email.message import EmailMessage
from datetime import datetime
import uuid
import qrcode
from PIL import Image
import io
import platform
import subprocess

st.set_page_config(page_title="🧳 Export Cockpit IA", layout="centered")
st.title("🧳 Valise Cockpit IA – Export, Partage & Historique")

# 🎞️ Animation valise
if os.path.exists("streamlit_app/images/valise.gif"):
    st.image("streamlit_app/images/valise.gif", caption="Préparation du bundle IA…", width=300)
else:
    st.info("📦 Animation valise manquante")

# 📦 Générer le bundle ZIP
if st.button("📁 Générer le bundle ZIP"):
    fichiers = [
        "logs/config_ia.json",
        "logs/status_env.json",
        "logs/config_log.txt",
        "streamlit_app/images/check.gif",
        "streamlit_app/images/error.gif",
        "streamlit_app/images/fusee.gif",
        "streamlit_app/images/valise.gif"
    ]
    try:
        with zipfile.ZipFile("logs/cockpit_bundle.zip", "w") as zipf:
            for f in fichiers:
                if os.path.exists(f):
                    zipf.write(f)
        st.image("streamlit_app/images/valise.gif", caption="🧳 Valise IA prête", width=250)
        st.success("✅ Bundle exporté dans `logs/cockpit_bundle.zip`")
    except Exception as e:
        st.error(f"❌ Erreur export ZIP : {e}")

# 🔌 Canal de notification depuis config
canal = "telegram"
try:
    with open("logs/config_ia.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    canal = config.get("notifications", {}).get("canal", "telegram")
except:
    st.warning("⚠️ Canal non détecté, défaut = Telegram")

# 📤 Partage automatique
if st.button("📤 Partager le bundle cockpit IA"):
    zip_path = "logs/cockpit_bundle.zip"
    if not os.path.exists(zip_path):
        st.error("❌ Le ZIP n’existe pas. Génère-le d’abord.")
    else:
        try:
            if canal == "telegram":
                token = st.secrets["telegram_token"]
                chat_id = st.secrets["telegram_chat_id"]
                with open(zip_path, "rb") as f:
                    r = requests.post(
                        f"https://api.telegram.org/bot{token}/sendDocument",
                        data={"chat_id": chat_id},
                        files={"document": f}
                    )
                st.success("✅ Valise cockpit envoyée via Telegram")

            elif canal == "email":
                sender = st.secrets["email_sender"]
                receiver = st.secrets["email_receiver"]
                password = st.secrets["email_password"]
                msg = EmailMessage()
                msg['Subject'] = "📤 Cockpit IA – Export de mission"
                msg['From'] = sender
                msg['To'] = receiver
                msg.set_content("Voici la valise cockpit IA exportée.")
                with open(zip_path, "rb") as f:
                    msg.add_attachment(f.read(), maintype='application', subtype='zip', filename="cockpit_bundle.zip")
                with smtplib.SMTP("smtp.gmail.com", 587) as server:
                    server.starttls()
                    server.login(sender, password)
                    server.send_message(msg)
                st.success("✅ Valise cockpit envoyée par Email")

            # 🔔 Notification sonore
            if platform.system() == "Windows":
                subprocess.call(["powershell", "-c", "[console]::beep(1000,300); [console]::beep(1400,400)"])

        except Exception as e:
            st.error(f"❌ Erreur d’envoi : {e}")

# 🗂️ Journalisation avec ID horodaté
if st.button("🗂️ Enregistrer export dans le journal"):
    export_id = str(uuid.uuid4())[:8]
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open("logs/exports_log.txt", "a", encoding="utf-8") as log:
            log.write(f"[{now}] Export ID: {export_id} – Valise cockpit IA\n")
        st.success(f"✅ Export enregistré – ID: `{export_id}`")
    except Exception as e:
        st.error(f"❌ Erreur journal export : {e}")

# 📜 Historique des exports
st.subheader("📜 Historique des exports cockpit IA")
if os.path.exists("logs/exports_log.txt"):
    with open("logs/exports_log.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()[-10:]
    for line in lines[::-1]:
        st.markdown(f"🧳 {line.strip()}")
else:
    st.info("📂 Aucun export enregistré")

# 📱 QR Code export ID
st.subheader("📱 QR Code export ID")

try:
    if os.path.exists("logs/exports_log.txt"):
        with open("logs/exports_log.txt", "r", encoding="utf-8") as f:
            last_line = f.readlines()[-1]
        id_export = last_line.split("Export ID:")[1].strip().split("–")[0].strip()
    else:
        id_export = "aucun"

    qr_data = f"Export cockpit IA – ID : {id_export}"
    img = qrcode.make(qr_data)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    st.image(buf, caption=f"QR Code export ID : {id_export}", width=250)

except Exception as e:
    st.error(f"❌ Impossible de générer le QR Code : {e}")