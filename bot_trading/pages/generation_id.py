import streamlit as st
import random

def generer_identite():
    prenoms = ["Léo", "Camille", "Noah", "Emma", "Lucas", "Chloé", "Nathan", "Lina"]
    noms = ["Durand", "Lefèvre", "Moreau", "Garcia", "Roux", "Fournier", "Mercier", "Faure"]
    villes = ["Paris", "Lyon", "Marseille", "Toulouse", "Nantes", "Strasbourg", "Bordeaux", "Lille"]
    metiers = ["Data Scientist", "Développeur IA", "Analyste Cybersécurité", "UX Designer", "Ingénieur Robotique"]

    identite = {
        "Prénom": random.choice(prenoms),
        "Nom": random.choice(noms),
        "Âge": random.randint(22, 45),
        "Ville": random.choice(villes),
        "Métier": random.choice(metiers),
        "Avatar": f"https://randomuser.me/api/portraits/{random.choice(['men', 'women'])}/{random.randint(1, 99)}.jpg"
    }

    return identite

def display():
    st.subheader("🎨 Génération d'identité IA")

    if st.button("🔁 Générer une nouvelle identité"):
        identite = generer_identite()

        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(identite["Avatar"], caption="Avatar IA", use_column_width=True)
        with col2:
            st.markdown(f"**Prénom :** {identite['Prénom']}")
            st.markdown(f"**Nom :** {identite['Nom']}")
            st.markdown(f"**Âge :** {identite['Âge']} ans")
            st.markdown(f"**Ville :** {identite['Ville']}")
            st.markdown(f"**Métier :** {identite['Métier']}")