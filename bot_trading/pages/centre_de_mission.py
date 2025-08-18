# streamlit_app/pages/centre_de_mission.py

import streamlit as st

def display():
    st.title("🎯 Centre de mission IA")
    st.markdown("""
        Bienvenue dans ton centre de mission personnalisé.  
        Ici, tu peux suivre les missions en cours, en démarrer de nouvelles, et voir ton niveau de progression.
    """)

    # Exemple de contenu dynamique
    st.subheader("📌 Missions disponibles")
    missions = ["Analyser les données clients", "Prévoir les ventes mensuelles", "Optimiser les campagnes marketing"]
    for mission in missions:
        st.checkbox(mission)

    st.subheader("📈 Statistiques")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Missions terminées", 12)
    with col2:
        st.metric("Niveau IA", "Expert 🧠")

    st.success("🚀 Prêt à lancer ta prochaine mission ?")

if __name__ == "__main__":
    display()