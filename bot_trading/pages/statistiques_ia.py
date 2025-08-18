import streamlit as st
import pandas as pd
import numpy as np
import os

def display():
    st.set_page_config(page_title="Statistiques IA", layout="wide")

    st.markdown("<h1 style='text-align:center; color:#00f0ff;'>📊 Statistiques IA</h1>", unsafe_allow_html=True)

    # 📈 Évolution du capital
    st.subheader("📈 Courbe du capital IA")
    try:
        df = pd.read_csv("logs/profit_log.csv")
        st.line_chart(df["capital"])
    except:
        st.warning("⚠️ Fichier 'profit_log.csv' introuvable ou format incorrect.")

    # 🧠 Score IA (simulation aléatoire)
    st.subheader("🧠 Performance IA")
    score = np.random.randint(70, 95)
    st.metric(label="Score IA", value=f"{score}%", delta=f"+{np.random.randint(1, 5)}%")
    st.progress(score / 100)

    # 📜 Historique diagnostic (CSV fictif ou réel)
    st.subheader("📜 Historique des diagnostics IA")
    hist_path = "logs/diagnostic_log.csv"
    if os.path.exists(hist_path):
        try:
            df_hist = pd.read_csv(hist_path)
            st.dataframe(df_hist, use_container_width=True)
        except:
            st.warning("⚠️ Erreur dans le fichier 'diagnostic_log.csv'.")
    else:
        st.info("ℹ️ Aucun diagnostic enregistré pour le moment.")

    # 🔍 Prévision IA simulée
    st.subheader("🔍 Prévision du capital IA")
    days = st.slider("Jours à prévoir :", 3, 30, 7)
    future = np.cumsum(np.random.randn(days) + 1.5) + 1000
    future_df = pd.DataFrame({"Prévision Capital": future})
    st.line_chart(future_df)

    # 📤 Export CSV
    st.subheader("📤 Exporter les statistiques IA")
    col1, col2 = st.columns(2)
    with col1:
        try:
            st.download_button("📁 Export CSV", data=df.to_csv(index=False), file_name="stats_ia.csv")
        except:
            st.warning("⚠️ Impossible d’exporter les données du capital.")
    with col2:
        st.button("🧾 Générer rapport PDF")  # Tu peux ajouter une vraie fonction plus tard