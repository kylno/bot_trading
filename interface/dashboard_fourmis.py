import json
import os

def charger_config(chemin="config/bot_config.json"):
    if not os.path.isfile(chemin):
        print(f"❌ Fichier introuvable : {chemin}")
        return {}
    try:
        with open(chemin, encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Erreur lors du décodage JSON.")
        return {}

def afficher_tableau_bots(bots_config):
    if not bots_config:
        print("⚠️ Aucune configuration de bots trouvée.")
        return

    print("\n📊 Dashboard des bots IA\n")
    print(f"{'Nom du Bot':<15} | {'Style':<15} | {'Trading':<20} | {'Risque':<12} | {'Capital (%)':<12}")
    print("-" * 80)

    for bot_nom, infos in bots_config.items():
        style = infos.get("style", "—")
        trading_type = infos.get("type", infos.get("objectif", "—"))
        risque = infos.get("risque", "—")
        capital = int(infos.get("capital_allocation", 0) * 100)
        print(f"{bot_nom:<15} | {style:<15} | {trading_type:<20} | {risque:<12} | {capital:<12}%")

    print("\n🧠 Dashboard terminé.\n")

def main():
    bots = charger_config()
    afficher_tableau_bots(bots)

if __name__ == "__main__":
    main()