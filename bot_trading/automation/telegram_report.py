import requests

# 🔐 RENSEIGNE TON TOKEN ET TON ID TÉLÉGRAM ICI
TOKEN = "8019499141:AAECJvxF6H4BQDqbSIO6INSBR9z7FQxaqys"  # ← Ton token API donné par BotFather
CHAT_ID = "6982878922"                            # ← Ton ID perso (via @userinfobot)
LOG_PATH = "logs/env_health.log"                 # ← Chemin vers ton fichier diagnostic

def extract_last_diagnostic():
    try:
        with open(LOG_PATH, "r", encoding="utf-8") as file:
            lines = file.readlines()
        last_block = []
        found_start = False
        for line in reversed(lines):
            if "Diagnostic IA" in line:
                found_start = True
            if found_start:
                last_block.insert(0, line.strip())
                if len(last_block) > 1 and "Diagnostic IA" in last_block[0]:
                    break
        return "\n".join(last_block) if last_block else "📋 Aucun diagnostic trouvé"
    except Exception as e:
        return f"❌ Erreur lors de la lecture du log : {e}"

def send_report():
    message = f"🧠 Rapport IA du jour\n\n{extract_last_diagnostic()}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("✅ Message envoyé sur Telegram")
        else:
            print(f"❌ Erreur Telegram : {response.text}")
    except Exception as e:
        print(f"❌ Exception d'envoi : {e}")

if __name__ == "__main__":
    send_report()