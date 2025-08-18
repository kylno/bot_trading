# scanner_ai.py

import time
from executor import buy, sell_all
from scoring_ai import choisir_meilleur_actif

def ia_decision_engine():
    """
    Fonction principale qui décide quoi faire selon le meilleur actif IA.
    - Si aucun actif valable ➤ retrait
    - Sinon ➤ achat automatique sur le meilleur actif
    """
    choix = choisir_meilleur_actif()

    if choix:
        buy(choix, 100)  # Montant fictif à investir
        return f"✅ IA investit sur {choix} selon score stratégique."
    else:
        sell_all()
        return "🛑 Aucun signal fiable ➤ désengagement IA."

# 🔁 Boucle en continu toutes les secondes
if __name__ == "__main__":
    print("🚀 IA stratégique autonome lancée.")
    while True:
        try:
            message = ia_decision_engine()
            print(message)
        except Exception as e:
            print(f"❌ Erreur dans le cycle IA : {str(e)}")
        time.sleep(1)