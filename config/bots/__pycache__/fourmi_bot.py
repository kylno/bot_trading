import time
import random
from dispatch.fourmi_dispatcher import assigner_fourmi, liberer_fourmi

def run_fourmi_bot(capital):
    print(f"\n🐜 FOURMI BOT ACTIVÉ — Capital : {capital}€ 🐜")

    opportunite = random.choice([True, False])
    if opportunite:
        print("🔍 Opportunité DCA repérée !")

        id_fourmi = assigner_fourmi("surveillance", "Fourmi")
        if id_fourmi:
            print(f"📦 Fourmi {id_fourmi} surveille actif + transfert micro-gain...")
            time.sleep(2)
            liberer_fourmi(id_fourmi)
            print("✅ Mission terminée.")
    else:
        print("📡 Aucun signal détecté. Fourmi en observation passive.")