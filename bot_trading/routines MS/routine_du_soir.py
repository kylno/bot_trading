import json
from datetime import datetime
from core.scoring_alertes import scorer_alertes
from core.triggers_bot import détecter_et_déclencher

# Charger la config
with open("config/config_ia.json", "r", encoding="utf-8") as f:
    config = json.load(f)

mode_vacances = config.get("vacances", False)

def routine_soir():
    chemin = "logs/alertes_raw.jsonl"
    try:
        with open(chemin, "r", encoding="utf-8") as f:
            alertes = [json.loads(l) for l in f.readlines()]
    except FileNotFoundError:
        alertes = []

    alertes_scored = scorer_alertes(alertes, mode_vacances=mode_vacances)

    with open("logs/alertes_scored.jsonl", "a", encoding="utf-8") as f:
        for a in alertes_scored:
            a["timestamp"] = datetime.now().isoformat()
            f.write(json.dumps(a) + "\n")

    détecter_et_déclencher(alertes_scored, mode_vacances=mode_vacances)
