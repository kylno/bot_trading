import streamlit as st

def bouton_validation():
    if st.button("✅ Valider"):
        st.session_state.validation_ok = True