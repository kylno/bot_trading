import shutil
import os
from datetime import datetime

def backup_cockpit():
    # 📁 Créer le dossier backups s'il n'existe pas
    os.makedirs("backups", exist_ok=True)

    # 🕒 Timestamp unique
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # 🗂️ Fichiers à sauvegarder (fichier source ➜ fichier destination horodaté)
    fichiers = {
        "config/config_ia.json": f"backups/config_{timestamp}.json",
        "logs/capital.jsonl": f"backups/capital_{timestamp}.jsonl",
        "logs/alertes.jsonl": f"backups/alertes_{timestamp}.jsonl",
        "logs/config_history.jsonl": f"backups/config_history_{timestamp}.jsonl",
        "logs/opportunites_crypto.json": f"backups/opportunites_crypto_{timestamp}.json"
    }

    # ✅ Copier les fichiers s'ils existent
    for src, dst in fichiers.items():
        if os.path.exists(src):
            shutil.copy(src, dst)
        else:
            print(f"[🛑] Fichier introuvable : {src}")