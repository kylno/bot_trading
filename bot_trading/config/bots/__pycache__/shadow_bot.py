import time
import random
from dispatch.fourmi_dispatcher import assigner_fourmi, liberer_fourmi

def run_shadow_bot(capital):
    print(f"\n🧠 SHADOW BOT ACTIVÉ — Capital : {capital}€ 🧠")

    signal_detecte = random.choice([True, False])
    if signal_detecte:
        print("📈 Signal stable détecté. Intervention tactique...")

        id_fourmi = assigner_fourmi("sentinelle", "Principal")
        if id_fourmi:
            print(f"👀 Fourmi {id_fourmi} observe actif + prépare position...")
            time.sleep(2)
            liberer_fourmi(id_fourmi)
            print("✅ Mission terminée.")
    else:
        print("🌫️ Aucun signal détecté. Shadow reste à l’affût.")