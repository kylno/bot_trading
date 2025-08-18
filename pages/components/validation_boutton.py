import streamlit as st

def bouton_validation(label="Valider l'action ✅", key="validation_ok"):
    # Injecter le CSS une seule fois
    if "css_injected" not in st.session_state:
        st.markdown("""
            <style>
            .custom-button {
                background-color: #4CAF50;
                color: white;
                padding: 12px 24px;
                font-size: 16px;
                border: none;
                border-radius: 8px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }
            .custom-button:hover {
                background-color: #45a049;
            }
            </style>
        """, unsafe_allow_html=True)
        st.session_state.css_injected = True

    # Formulaire avec bouton stylisé
    with st.form(f"form_{key}"):
        st.markdown(f'<button class="custom-button" type="submit">{label}</button>', unsafe_allow_html=True)
        submitted = st.form_submit_button("")
        if submitted:
            st.session_state[key] = True