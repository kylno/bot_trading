# ia_network.py
# Cerveau collectif du réseau IA distribué

import threading

# État global de l'IA (peut être enrichi dynamiquement)
ia_state = {
    "niveau_IA": "stable",
    "sécurité": "active",
    "agents_actifs": [],
    "historique": []
}

state_lock = threading.Lock()

def get_state():
    """Retourne une copie de l'état global IA"""
    with state_lock:
        return ia_state.copy()

def update_state(key, value):
    """Met à jour un élément de l'état global IA"""
    with state_lock:
        ia_state[key] = value
        ia_state["historique"].append((key, value))

def add_agent(nom_agent):
    """Ajoute un agent IA actif au réseau"""
    with state_lock:
        if nom_agent not in ia_state["agents_actifs"]:
            ia_state["agents_actifs"].append(nom_agent)
            ia_state["historique"].append(("nouvel_agent", nom_agent))