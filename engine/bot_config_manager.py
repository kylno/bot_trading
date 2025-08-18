import json
import os

def charger_config(nom_bot):
    """
    Charge le fichier de configuration JSON correspondant au bot donné.

    :param nom_bot: Nom du bot (ex: 'berserk')
    :return: Dictionnaire de configuration
    """
    chemin = os.path.join("config", f"config_{nom_bot}.json")

    if not os.path.exists(chemin):
        raise FileNotFoundError(f"❌ Fichier de configuration introuvable : {chemin}")

    with open(chemin, "r", encoding="utf-8") as f:
        config = json.load(f)

    return config