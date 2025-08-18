import json
import subprocess
from datetime import datetime
import os
from core.historique_reco import enregistrer_reco

# 📦 Fichier d'alertes scorées
ALERTES_PATH = "logs/alertes_scored.json"

# 🧠 Seuil de déclenchement
SEUIL = 90

# 🤖 Mapping actif → bot
ACTIF_BOT = {
    "bitcoin": "Berzerk+",
    "eth": "Shadow",
    "solana": "Fourmi",
    "apple": "Casa de Papel",
    "nasdaq": "Casa de Papel",
    "gold": "GoldHunter"
}

def charger_alertes():
    if os.path.exists(ALERTES_PATH):
        with open(ALERTES_PATH, encoding="utf-8") as f:
            return json.load(f)
    return []

def détecter_et_déclencher(alertes):
    for a in alertes:
        score = a.get("score", 0)
        texte = a.get("texte", "").lower()

        if score >= SEUIL:
            actif = next((k for k in ACTIF_BOT if k in texte), None)
            if actif:
                bot = ACTIF_BOT[actif]
                print(f"🚀 Déclenchement du bot {bot} sur {actif} (score {score})")

                # 🔧 Lancement du bot (à adapter selon ton système)
                subprocess.run(["python", "modules/executor.py", "--bot", bot])

                # 🧾 Enregistrement dans l’historique
                enregistrer_reco(
                    bot=bot,
                    actif=actif,
                    score=score,
                    raison=f"Alerte détectée : {a['texte']}",
                    action="Déclenchement automatique"
                )

def run_trigger():
    alertes = charger_alertes()
    détecter_et_déclencher(alertes)

# 🚀 Exécution directe
if __name__ == "__main__":
    run_trigger()