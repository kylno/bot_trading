import csv
import os
from datetime import datetime
import random

def generer_mission_auto():
    fourmi_id = f"fourmi_{random.randint(100, 999)}"
    type_mission = random.choice(["analyse", "veille", "exploration", "renseignement"])
    status = random.choice(["terminée", "en cours", "en échec"])
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ligne = [fourmi_id, type_mission, status, timestamp]

    chemin_logs = "data/logs.csv"
    os.makedirs(os.path.dirname(chemin_logs), exist_ok=True)

    fichier_existe = os.path.isfile(chemin_logs)
    with open(chemin_logs, "a", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        if not fichier_existe:
            writer.writerow(["ID", "Type", "Statut", "Horodatage"])
        writer.writerow(ligne)

    print(f"📦 Mission attribuée à {fourmi_id} : {type_mission}")

def generer_missions_multiples(nb=3):
    print(f"🧠 Génération de {nb} missions IA en cours...")
    for _ in range(nb):
        generer_mission_auto()