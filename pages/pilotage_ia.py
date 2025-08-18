import streamlit as st
import pandas as pd
import numpy as np
import subprocess
import io
import zipfile
import os

def verifier_et_corriger_structure():
    structure_attendue = {
        "automation": ["auto_env_check.py"],
        "logs": [],
        "streamlit_app": ["style.css", "centre_de_mission.py"],
        "streamlit_app/images": ["checklist.gif", "intro_cockpit.gif", "security.gif"],
        "streamlit_app/pages": ["statistiques_ia.py", "diagnostic_ia.py", "pilotage_ia.py"],
        ".": ["main.py", "menu.py"]
    }

    messages = []
    corrections = []
    tout_est_bon = True

    for dossier, fichiers in structure_attendue.items():
        if dossier != "." and not os.path.exists(dossier):
            os.makedirs(dossier)
            corrections.append(f"📂 Dossier créé : {dossier}")

        for fichier in fichiers:
            chemin = os.path.join(dossier, fichier)
            if os.path.exists(chemin):
                messages.append(f"✅ {chemin}")
            else:
                messages.append(f"❌ {chemin} manquant")
                tout_est_bon = False

    rapport = "\n".join(messages + corrections)
    return rapport, tout_est_bon

def zip_cockpit_files():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as z:
        for file in [
            "logs/profit_log.csv",
            "streamlit_app/images/checklist.gif",
            "streamlit_app/centre_de_mission.py",
            "streamlit_app/pages/statistiques_ia.py",
            "streamlit_app/pages/diagnostic_ia.py",
            "automation/auto_env_check.py"
        ]:
            if os.path.exists(file):
                z.write(file)
    buffer.seek(0)
    return buffer

def display():
    st.set_page_config(page_title="Pilotage IA Central", layout="wide")
    st.markdown("<h1 style='text-align:center; color:#00f0ff;'>🧠 Pilotage IA – Poste de Commande</h1>", unsafe_allow_html=True)

    if "firewall_active" not in st.session_state:
        st.session_state["firewall_active"] = False

    st.subheader("📊 Capital IA")
    try:
        df = pd.read_csv("logs/profit_log.csv")
        st.line_chart(df["capital"])
    except:
        st.warning("⚠️ Fichier 'profit_log.csv' manquant")

    st.subheader("💼 Portefeuille crypto")
    portefeuille = {"Bitcoin": "2.5 BTC", "Ethereum": "14 ETH", "Solana": "160 SOL", "USDT": "$3,500"}
    cols = st.columns(len(portefeuille))
    for i, (asset, value) in enumerate(portefeuille.items()):
        with cols[i]: st.metric(label=asset, value=value)

    st.subheader("⚡ Énergie cognitive IA")
    niveau_ia = np.random.randint(30, 100)
    st.metric("🧬 Niveau IA", f"{niveau_ia}%", delta=f"+{np.random.randint(1,5)}%")
    st.progress(niveau_ia / 100)

    st.subheader("📋 Checklist cockpit IA")
    gif_path = "streamlit_app/images/checklist.gif"
    if os.path.exists(gif_path):
        st.image(gif_path, use_container_width=True)
    else:
        st.info("ℹ️ Checklist visuelle manquante")

    st.subheader("🔐 Sécurité IA – Firewall")
    if st.button("🛡️ Activer le bouclier IA"):
        st.session_state["firewall_active"] = True
        st.success("🧠 Sécurité IA activée")
    elif st.session_state["firewall_active"]:
        st.info("✅ Firewall IA actif")
    else:
        st.info("🧬 En attente d’activation...")

    if st.session_state["firewall_active"]:
        security_gif = "streamlit_app/images/security.gif"
        if os.path.exists(security_gif):
            st.image(security_gif, caption="🔒 Firewall IA activé", use_container_width=True)

    st.subheader("🧪 Diagnostic IA")
    if st.session_state["firewall_active"]:
        if st.button("🔍 Lancer le diagnostic système"):
            try:
                result = subprocess.run(["python", "automation/auto_env_check.py"], capture_output=True, text=True)
                st.text_area("📋 Rapport diagnostic", result.stdout, height=300)
                st.success("✅ Diagnostic terminé")
            except Exception as e:
                st.error(f"❌ Erreur lors du diagnostic : {e}")
    else:
        st.warning("🛡️ Active d’abord la sécurité IA pour autoriser le scan")

    st.subheader("📦 Export cockpit IA")
    if st.session_state["firewall_active"]:
        st.warning("🚫 Export désactivé pendant que le bouclier est actif")
    else:
        st.download_button(
            "📁 Télécharger cockpit (ZIP)",
            data=zip_cockpit_files(),
            file_name="cockpit_kylian.zip"
        )

    st.subheader("📁 Vérification & réparation structure IA")
    if st.button("🧠 Scanner et corriger la structure"):
        rapport, ok = verifier_et_corriger_structure()
        st.text_area("📋 Résultat du scan", rapport, height=300)
        if ok:
            st.success("✅ Structure complète")
        else:
            st.warning("⚠️ Structure IA réparée partiellement")

    intro_path = "streamlit_app/images/intro_cockpit.gif"
    if os.path.exists(intro_path):
        st.image(intro_path, caption="🚀 Cockpit IA prêt", use_container_width=True)

    st.markdown("---")
    st.markdown("<div style='text-align:center; color:#888;'>🧠 Interface IA | Commandant : <strong>Kylian</strong></div>", unsafe_allow_html=True)