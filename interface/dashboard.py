import json
import os

CONFIG_PATH = "config/bot_config.json"

def charger_config(chemin=CONFIG_PATH):
    """Charge les données du fichier JSON des bots."""
    if not os.path.isfile(chemin):
        print(f"❌ Fichier introuvable : {chemin}")
        return {}
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Erreur : fichier JSON mal formé.")
        return {}

def afficher_dashboard(bots):
    """Affiche le tableau terminal des bots IA."""
    if not bots:
        print("⚠️ Aucun bot disponible dans la configuration.")
        return

    print("\n📊 Dashboard IA — Profils bots\n")
    print(f"{'Nom':<12} | {'Style':<15} | {'Type/objectif':<20} | {'Risque':<12} | {'Capital (%)':<12}")
    print("-" * 80)

    for nom, infos in bots.items():
        style = infos.get("style", "—")
        type_trading = infos.get("type", infos.get("objectif", "—"))
        risque = infos.get("risque", "—")
        capital = int(infos.get("capital_allocation", 0) * 100)

        print(f"{nom:<12} | {style:<15} | {type_trading:<20} | {risque:<12} | {capital:<12}%")

    print("\n🧠 Dashboard terminé.\n")

def main():
    bots = charger_config()
    afficher_dashboard(bots)

if __name__ == "__main__":
    main()