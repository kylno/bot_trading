import json
from datetime import datetime
import requests

def envoyer_rapport_telegram(token, chat_id):
    try:
        with open("logs/rapport_capital.pdf", "rb") as f:
            files = {"document": f}
            url = f"https://api.telegram.org/bot{token}/sendDocument"
            data = {"chat_id": chat_id}
            response = requests.post(url, data=data, files=files)
            return response.status_code == 200
    except:
        return False

def envoyer_alerte_telegram(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    response = requests.post(url, data=data)
    return response.status_code == 200

def enregistrer_alerte(type_alerte, message):
    log = {
        "timestamp": datetime.now().isoformat(),
        "type": type_alerte,
        "message": message
    }
    with open("logs/alertes.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(log) + "\n")