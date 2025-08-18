import json
from datetime import datetime
import os

# 📄 Fichier de log des recommandations IA
HISTO_PATH = "logs/historique_reco.jsonl"

# 🧠 Fonction d'enregistrement
def enregistrer_reco(bot, actif, score, raison, action):
    reco = {
        "timestamp": datetime.now().isoformat(),
        "bot": bot,
        "actif": actif,
        "score": score,
        "raison": raison,
        "action_suggérée": action
    }

    try:
        # Crée le dossier logs si nécessaire
        os.makedirs(os.path.dirname(HISTO_PATH), exist_ok=True)

        # Ajoute la reco au fichier JSONL
        with open(HISTO_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(reco) + "\n")
        print(f"✅ Recommandation enregistrée pour {bot} sur {actif}")
    except Exception as e:
        print("❌ Erreur enregistrement reco :", e)

# 🚀 Exemple d'utilisation
if __name__ == "__main__":
    enregistrer_reco(
        bot="Berzerk+",
        actif="Bitcoin",
        score=92,
        raison="Pump détecté + mentions X + volume élevé",
        action="Entrée agressive"
    )