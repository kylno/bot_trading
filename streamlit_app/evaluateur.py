# evaluateur.py
# Évalue les performances du système IA

from ia_network import get_state

def run():
    état = get_state()
    score = état.get("score_decision", 0.0)
    erreurs = état.get("erreurs_detectées", 0)

    print(f"🧪 Score IA : {score:.2f}")
    print(f"⚠️ Erreurs détectées : {erreurs}")

    if score < 0.5 or erreurs > 3:
        print("❌ Performance insuffisante.")
    else:
        print("✅ Performance stable.")