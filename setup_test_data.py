import json
from datetime import datetime, timedelta
import os

os.makedirs("logs", exist_ok=True)
os.makedirs("config", exist_ok=True)

# Capital.jsonl
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

# Investissements.json
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

# Config IA
config = {"vacances": False}
with open("config/config_ia.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)

print("✅ Données de test générées avec succès.")