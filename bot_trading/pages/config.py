import streamlit as st
import json
import os
import base64
from datetime import datetime
import qrcode
from PIL import Image

st.set_page_config(page_title="🔧 Configuration IA", layout="centered")
st.title("🔧 Paramètres du cockpit IA")

config_path = "logs/config_ia.json"
log_path = "logs/config_log.txt"

default_config = {
    "version": "1.0",
    "auteur": "Kylian",
    "mode_diagnostic": True,
    "niveau_severite": "standard",
    "notifications": {
        "canal": "telegram",
        "envoyer_si_erreur": True,
        "envoyer_rapport": False
    },
    "auto_blocage": {
        "actif": True,
        "seuil_erreurs": 3
    },
    "visuel": {
        "theme": "dark",
        "animations": True
    }
}

if os.path.exists(config_path):
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
else:
    config = default_config

# Formulaire
st.subheader("📌 Infos générales")
version = st.text_input("Version IA", value=config.get("version"))
auteur = st.text_input("Nom du pilote", value=config.get("auteur"))

st.subheader("🧪 Diagnostic")
mode_diagnostic = st.checkbox("Activer le diagnostic", value=config.get("mode_diagnostic"))
niveau_severite = st.selectbox("Sévérité", ["standard", "strict", "relax"],
    index=["standard", "strict", "relax"].index(config.get("niveau_severite")))

st.subheader("📬 Notifications")
notif_cfg = config.get("notifications", {})
canal = st.selectbox("Canal", ["telegram", "email"],
    index=["telegram", "email"].index(notif_cfg.get("canal")))
notif_erreur = st.checkbox("Envoyer en cas d’erreur", value=notif_cfg.get("envoyer_si_erreur"))
notif_rapport = st.checkbox("Envoyer le rapport complet", value=notif_cfg.get("envoyer_rapport"))

st.subheader("⛔ Auto-blocage")
blocage_cfg = config.get("auto_blocage", {})
blocage_actif = st.checkbox("Activer le blocage auto", value=blocage_cfg.get("actif"))
seuil_erreurs = st.slider("Seuil avant blocage", 1, 10, value=blocage_cfg.get("seuil_erreurs"))

st.subheader("🎨 Visuel")
visuel_cfg = config.get("visuel", {})
theme = st.selectbox("Thème", ["dark", "light"],
    index=["dark", "light"].index(visuel_cfg.get("theme")))
animations = st.checkbox("Activer les animations", value=visuel_cfg.get("animations"))

# Boutons
col1, col2 = st.columns(2)

with col1:
    if st.button("💾 Sauvegarder la configuration"):
        new_config = {
            "version": version,
            "auteur": auteur,
            "mode_diagnostic": mode_diagnostic,
            "niveau_severite": niveau_severite,
            "notifications": {
                "canal": canal,
                "envoyer_si_erreur": notif_erreur,
                "envoyer_rapport": notif_rapport
            },
            "auto_blocage": {
                "actif": blocage_actif,
                "seuil_erreurs": seuil_erreurs
            },
            "visuel": {
                "theme": theme,
                "animations": animations
            }
        }

        try:
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(new_config, f, indent=2, ensure_ascii=False)
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(log_path, "a", encoding="utf-8") as log:
                log.write(f"[{now}] Sauvegarde par {auteur} – v{version}\n")
            st.success("✅ Configuration mise à jour")
        except Exception as e:
            st.error(f"❌ Erreur : {e}")

with col2:
    if st.button("♻️ Restaurer valeurs par défaut"):
        try:
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump(default_config, f, indent=2, ensure_ascii=False)
            st.success("✅ Paramètres restaurés")
        except Exception as e:
            st.error(f"❌ Échec restauration : {e}")

# Récapitulatif
st.subheader("📊 Récapitulatif actif")
try:
    with open(config_path, "r", encoding="utf-8") as f:
        conf = json.load(f)
    st.markdown(f"""
    **🔧 Version :** `{conf['version']}`  
    **👤 Auteur :** `{conf['auteur']}`  
    **🧪 Diagnostic :** `{"Oui" if conf['mode_diagnostic'] else "Non"}`  
    **⚠️ Sévérité :** `{conf['niveau_severite']}`  
    **📨 Canal :** `{conf['notifications']['canal']}`  
    **⛔ Blocage auto :** `{"Oui" if conf['auto_blocage']['actif'] else "Non"}`  
    **📉 Seuil erreurs :** `{conf['auto_blocage']['seuil_erreurs']}`  
    **🎨 Thème :** `{conf['visuel']['theme']}`  
    **🎞️ Animations :** `{"Activées" if conf['visuel']['animations'] else "Désactivées"}`
    """)
except:
    st.warning("⚠️ Impossible d’afficher la configuration")

# Téléchargement config
st.subheader("📥 Télécharger configuration")
if os.path.exists(config_path):
    with open(config_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    href = f'<a href="data:file/json;base64,{b64}" download="config_ia.json">🧾 Télécharger config_ia.json</a>'
    st.markdown(href, unsafe_allow_html=True)

# QR Code mobile
st.subheader("📱 QR Code configuration")
try:
    with open(config_path, "r", encoding="utf-8") as f:
        config_text = f.read()
    qr = qrcode.make(config_text)
    st.image(qr, caption="Scannez pour lire la configuration IA", width=250)
except Exception as e:
    st.error(f"❌ QR code non généré : {e}")