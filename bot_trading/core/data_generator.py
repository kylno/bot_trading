import json, os
from datetime import datetime, timedelta

def generer_donnees_test():
    os.makedirs("logs", exist_ok=True)
    os.makedirs("config", exist_ok=True)

    capital = []
    base = 100000
    for i in range(4):
        capital.append({
            "timestamp": (datetime.now() - timedelta(days=3 - i)).isoformat(),
            "capital": base + i * 24000
        })
    with open("logs/capital.jsonl", "w", encoding="utf-8") as f:
        for entry in capital:
            f.write(json.dumps(entry) + "\n")

    investissements = {
        "Immobilier locatif": "€250K",
        "Entreprise physique": "€45K",
        "Start-up": "€30K",
        "ETF": "€10K",
        "PORET": "+372%",
        "PO": "1000M"
    }
    with open("logs/investissements.json", "w", encoding="utf-8") as f:
        json.dump(investissements, f, indent=2)

    config = {
        "vacances": False,
        "seuil_capital": 50000,
        "seuil_variation": 10
    }
    with open("config/config_ia.json", "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)