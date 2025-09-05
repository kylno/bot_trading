import requests

def get_bot_config():
    try:
        response = requests.get("https://api.exemple.com/bot_config")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erreur API bot_config : {e}")
        return {}

def get_performance():
    try:
        response = requests.get("https://api.exemple.com/performance")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erreur API performance : {e}")
        return {}

def get_alerts():
    try:
        response = requests.get("https://api.exemple.com/alerts")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erreur API alerts : {e}")
        return []