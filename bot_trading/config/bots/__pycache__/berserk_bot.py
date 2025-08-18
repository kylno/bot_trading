import time
import random
from dispatch.fourmi_dispatcher import assigner_fourmi, liberer_fourmi

def run_berserk_bot(capital):
    print(f"\n🔥 BERSERK BOT ACTIVÉ — Capital : {capital}€ 🔥")

    # Simulation de détection d’un pump
    pump_detected = random.choice([True, False])
    if pump_detected:
        print("🚨 Pump détecté ! Exécution rapide...")

        id_fourmi = assigner_fourmi("transfert", "Berserk")

        if id_fourmi:
            print(f"💸 Fourmi {id_fourmi} effectue extraction des bénéfices...")
            time.sleep(2)
            liberer_fourmi(id_fourmi)
            print("✅ Mission terminée.")
    else:
        print("🔎 Aucun pump détecté. Aucun mouvement lancé.")