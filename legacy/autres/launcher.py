import time
from threading import Thread
from dispatch.berserk_bot import berserk_bot
from dispatch.fourmi_bot import fourmi_bot
from dispatch.shadow_bot import shadow_bot
from dispatch.fourmi_dispatcher import afficher_statut
import decision_engine

def lancer_escouade():
    print("\n💼 DÉMARRAGE DE LA FOURMILIÈRE TACTIQUE 💼")
    print("============================================")
    print("🧠 Principal (Shadow Bot) → Surveillance stratégique")
    print("🐜 Fourmi Bot → Opportunités lentes")
    print("💥 Berserk Bot → Réactions brutales aux pumps")
    print("🧠 Decision Engine → Analyse autonome des événements\n")

    # Lancement des bots en parallèle
    Thread(target=shadow_bot).start()
    Thread(target=fourmi_bot).start()
    Thread(target=berserk_bot).start()
    Thread(target=lancer_decision_engine).start()

    # Affichage de la fourmilière au démarrage
    print("📋 État initial des fourmis :")
    afficher_statut()
    print("\n✅ Tous les bots sont en route.\n")

def lancer_decision_engine():
    while True:
        decision_engine.prendre_decision()
        time.sleep(60)  # toutes les 60 secondes

if __name__ == "__main__":
    lancer_escouade()