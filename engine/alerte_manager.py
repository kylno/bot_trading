import os
from datetime import datetime

def envoyer_alerte(bot_name, message, niveau="INFO"):
    """
    Affiche une alerte dans la console et l'enregistre dans un fichier log dédié.

    :param bot_name: Nom du bot concerné (ex : 'berserk')
    :param message: Message d'alerte à afficher et sauvegarder
    :param niveau: Niveau de gravité ('INFO', 'WARNING', 'ERROR', 'CRITICAL')
    """
    horodatage = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    texte_final = f"[{horodatage}] [{niveau}] [{bot_name.upper()}] {message}"

    # Affichage console
    print(f"🚨 {texte_final}")

    # Chemin du fichier log
    dossier = "logs"
    os.makedirs(dossier, exist_ok=True)
    chemin_log = os.path.join(dossier, f"alerts_{bot_name.lower()}.log")

    # Enregistrement dans le fichier
    try:
        with open(chemin_log, "a", encoding="utf-8") as f:
            f.write(texte_final + "\n")
    except Exception as e:
        print(f"❌ Erreur lors de l’écriture du log d’alerte : {e}")