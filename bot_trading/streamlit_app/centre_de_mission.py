import streamlit as st
import pandas as pd
from PIL import Image
import os

def display():
    st.set_page_config(page_title="Centre de Mission", layout="wide")

    # 🌌 Fond animé via CSS
    with open("streamlit_app/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # 🧠 Titre
    st.markdown("<h1 style='text-align:center; color:#00f0ff;'>🧠 Cockpit IA – Centre de Mission</h1>", unsafe_allow_html=True)

    # 📈 Courbe du capital
    st.subheader("📊 Évolution du capital IA")
    capital_path = "logs/profit_log.csv"
    if os.path.exists(capital_path):
        df = pd.read_csv(capital_path)
        if "capital" in df.columns:
            st.line_chart(df["capital"])
        else:
            st.warning("⚠️ Le fichier CSV n’a pas de colonne 'capital'.")
    else:
        st.warning("⚠️ Fichier 'profit_log.csv' introuvable dans logs/.")

    # 💼 Portefeuille IA
    st.subheader("💼 Portefeuille IA")
    portefeuille = {
        "Bitcoin": "2.5 BTC",
        "Ethereum": "14 ETH",
        "Solana": "160 SOL",
        "USDT": "$3,500",
    }
    cols = st.columns(len(portefeuille))
    for i, (asset, value) in enumerate(portefeuille.items()):
        with cols[i]:
            st.metric(label=f"🪙 {asset}", value=value)

    # 🔘 Modules IA
    st.subheader("🧪 Actions IA")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔄 Relancer le diagnostic IA"):
            st.success("✅ Diagnostic IA lancé !")
    with col2:
        st.download_button("📤 Exporter cockpit IA", data="Export de données cockpit", file_name="cockpit_Kylian.zip")

    # 📋 Checklist animée IA
    st.subheader("📋 Modules activés")
    checklist_path = "streamlit_app/images/checklist.gif"
    if os.path.exists(checklist_path):
        st.image(checklist_path, use_container_width=True)
    else:
        st.info("ℹ️ Checklist cockpit IA non trouvée.")

    # 🎞️ Animation d’intro cockpit
    intro_path = "streamlit_app/images/intro_cockpit.gif"
    if os.path.exists(intro_path):
        st.image(intro_path, caption="✅ Cockpit IA activé", use_container_width=True)