import streamlit as st
from pages.pilotage_ia import display as pilotage_display
from pages.generation_id import display as generation_display
from pages.centre_de_mission import display as mission_display

def menu():
    menu_items = [
        "🧠 Pilotage IA",
        "🎨 Génération d'identité",
        "🎯 Centre de mission",
    ]

    choice = st.sidebar.radio("Navigation", menu_items)

    st.sidebar.image("images/intro_cockpit.gif", use_container_width=True)

    if choice == "🧠 Pilotage IA":
        pilotage_display()

    elif choice == "🎨 Génération d'identité":
        generation_display()

    elif choice == "🎯 Centre de mission":
        mission_display()