import os
import streamlit as st

VISUELS_STATUT = {
    "succès": ("fusee.gif", "Succès du cockpit 🚀"),
    "erreur": ("error.gif", "Des IA sont inactives ❌"),
    "attente": ("loading.gif", "Chargement en cours ⏳"),
    "valide": ("check.gif", "Validation système ✅"),
}

def afficher_visuel_statut(statut):
    """
    Affiche automatiquement le visuel correspondant au statut donné.
    """
    if statut in VISUELS_STATUT:
        nom_fichier, caption = VISUELS_STATUT[statut]
        chemin = os.path.join("images", nom_fichier)
        if os.path.exists(chemin):
            st.image(chemin, caption=caption, use_column_width=True)
        else:
            st.warning(f"Image introuvable : {chemin}")
    else:
        st.warning(f"Statut inconnu : {statut}")