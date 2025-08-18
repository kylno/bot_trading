import os
import time
import hashlib
from datetime import datetime

# 🛠️ Fichiers à surveiller
fichiers_critiques = [
    "bots/berserk_bot.py",
    "config/config_berserk.json"
]

# 🔐 On stocke ici les empreintes initiales (hash SHA256 de chaque fichier)
empreintes_fichiers = {}

def calculer_hash(path):
    try:
        with open(path, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()
    except FileNotFoundError:
        return None

def initialiser_surveillance():
    for fichier in fichiers_critiques:
        empreintes_fichiers[fichier] = calculer_hash(fichier)

def verifier_integrite():
    for fichier in fichiers_critiques:
        hash_actuel = calculer_hash(fichier)
        hash_initial = empreintes_fichiers.get(fichier)

        if hash_actuel and hash_initial and hash_actuel != hash_initial:
            horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"🚨 [{horodatage}] ALERTE : Le fichier '{fichier}' a été modifié !")

def boucle_surveillance(intervalle=10):
    print("🛡️ Surveillance de sécurité activée...\n")
    initialiser_surveillance()

    while True:
        verifier_integrite()
        time.sleep(intervalle)