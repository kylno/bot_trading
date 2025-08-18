from engine.bot_config_manager import charger_config

config = charger_config("berserk")

if not config["actif"]:
    print("⏸️ Le bot Berserk est désactivé via sa configuration.")
    exit()

# Exemple d’utilisation :
print(f"🎯 Token ciblé : {config['token_cible']}")
print(f"🚀 Seuil de variation : {config['seuil_variation']} %")
import json
import os

def charger_config(bot_name):
    """
    Charge le fichier de configuration correspondant à un bot donné.
    Applique des valeurs par défaut si des clés sont manquantes ou si le fichier est absent.
    """
    chemin = f"config/config_{bot_name.lower()}.json"

    # Valeurs par défaut universelles
    config_defaut = {
        "bot_name": bot_name,
        "token_cible": "BTC/USDT",
        "seuil_variation": 1.0,
        "pourcentage_entree": 0.5,
        "pourcentage_sortie": 0.5,
        "intervalle_scan": 5,             # en secondes
        "mode_securite": True,
        "alertes": True,
        "actif": True
    }

    if not os.path.exists(chemin):
        print(f"⚠️ Aucun fichier de config trouvé pour {bot_name}. Utilisation des valeurs par défaut.")
        return config_defaut

    try:
        with open(chemin, "r", encoding="utf-8") as f:
            config_utilisateur = json.load(f)

        # Fusion sécurisée : si une clé manque → valeur par défaut
        config_complet = config_defaut.copy()
        config_complet.update(config_utilisateur)

        return config_complet

    except Exception as e:
        print(f"🚨 Erreur de chargement pour {chemin} : {e}")
        print("⛑️ Utilisation de la configuration par défaut.")
        return config_defaut