import streamlit as st
import subprocess
import os
import pandas as pd
import time

def display():
    st.set_page_config(page_title="Diagnostic IA", layout="wide")
    st.markdown("<h1 style='text-align:center; color:#00f0ff;'>🧪 Diagnostic IA</h1>", unsafe_allow_html=True)

    st.subheader("📋 Description")
    st.markdown("Ce module analyse ton environnement IA, vérifie les fichiers, dépendances, et modules activés.")

    # 🔘 Lancer le vrai script
    if st.button("🔄 Lancer le diagnostic réel"):
        st.info("🔍 Diagnostic IA en cours...")
        try:
            # Appel du script Python réel
            result = subprocess.run(
                ["python", "automation/auto_env_check.py"],
                capture_output=True,
                text=True
            )
            # ✅ Résultat affiché dans Streamlit
            st.success("✅ Diagnostic terminé")
            st.text_area("🧠 Rapport du script", result.stdout if result.stdout else "Aucun résultat", height=300)
            # Sauvegarde du log dans CSV (optionnel)
            with open("logs/diagnostic_log.csv", "a", encoding="utf-8") as f:
                f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')},{'Succès' if result.returncode == 0 else 'Erreur'}\n")
        except Exception as e:
            st.error(f"❌ Erreur lors du diagnostic : {e}")

    # 📜 Affichage historique
    st.subheader("📜 Historique des diagnostics")
    hist_path = "logs/diagnostic_log.csv"
    if os.path.exists(hist_path):
        hist_df = pd.read_csv(hist_path, header=None, names=["Horodatage", "Statut"])
        st.dataframe(hist_df, use_container_width=True)
    else:
        st.info("ℹ️ Aucun historique trouvé.")