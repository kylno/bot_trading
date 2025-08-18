# alerte_discord.py
import requests
import json

# 🔗 Remplace ceci par TON URL WEBHOOK Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/XXXXXXXXXX/XXXXXXXXXXXX"

def lire_mode_auto():
    """Lit le mode actuel (auto ou manuel) depuis le fichier config_mode.json"""
    try:
        with open("config_mode.json", 'r') as f:
            config = json.load(f)
            return config.get("auto_mode", False)
    except:
        return False

def envoyer_alerte(symbol, variation):
    """Envoie une alerte formatée dans Discord via webhook"""
    mode = "AUTO 🤖" if lire_mode_auto() else "MANUEL 🧠"
    message = (
        f"🚨 **Pump détecté sur `{symbol.upper()}`**\n"
        f"📈 Variation: +{variation:.2f}% en 60 secondes\n"
        f"🎛️ Mode actuel : {mode}"
    )
    try:
        response = requests.post(WEBHOOK_URL, json={"content": message})
        if response.status_code == 204:
            print(f"📣 Alerte Discord envoyée pour {symbol.upper()}")
        else:
            print("⚠️ Réponse Discord inattendue :", response.status_code)
    except Exception as e:
        print("❌ Erreur d’envoi Discord :", e)