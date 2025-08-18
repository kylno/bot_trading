import json
import os

def get_bot_profile(bot_name, chemin_json="config/bot_config.json"):
    if not os.path.isfile(chemin_json):
        print(f"❌ Fichier introuvable : {chemin_json}")
        return

    with open(chemin_json, encoding="utf-8") as f:
        data = json.load(f)

    profile = data.get(bot_name)
    if not profile:
        print(f"⚠️ Bot '{bot_name}' non défini dans le fichier de config.")
        return

    print(f"\n📘 Profil technique de '{bot_name}' :\n")
    for key, value in profile.items():
        print(f" - {key.replace('_', ' ').capitalize()}: {value}")
    print("\n🧠 Chargement terminé.\n")