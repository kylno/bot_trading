import csv
import os
import random
from datetime import datetime, timedelta

def generer_nom_ia():
    préfixes = ["Zeta", "Alpha", "Nova", "Omega", "Delta", "Neuro", "Proto"]
    suffixes = ["Fourmi", "Sentinelle", "Drone", "Analyseur", "Explorateur"]
    numero = random.randint(1, 99)

    nom = f"{random.choice(préfixes)}{random.choice(suffixes)}-{numero}"
    print(f"🔤 Nom IA généré : {nom}")
    return nom

def simuler_colonie():
    chemin_logs = "data/logs.csv"
    os.makedirs(os.path.dirname(chemin_logs), exist_ok=True)
    fichier_existe = os.path.isfile(chemin_logs)

    with open(chemin_logs, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not fichier_existe:
            writer.writerow(["ID", "Type", "Statut", "Horodatage"])

        for i in range(10):
            fourmi_id = f"fourmi_{random.randint(100, 999)}"
            mission = random.choice(["analyse", "veille", "exploration", "détection"])
            statut = random.choice(["terminée", "en cours", "inactif"])
            date = datetime.now() - timedelta(days=random.randint(0, 10))
            writer.writerow([fourmi_id, mission, statut, date.strftime("%Y-%m-%d %H:%M:%S")])

    print("🧪 Colonie simulée avec 10 entrées IA.")

def detecter_ia_inactives():
    chemin_logs = "data/logs.csv"
    if not os.path.exists(chemin_logs):
        print("❌ Aucun journal trouvé pour analyse.")
        return

    with open(chemin_logs, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        lignes = list(reader)

    if len(lignes) <= 1:
        print("📭 Aucune donnée IA à analyser.")
        return

    inactives = [ligne for ligne in lignes[1:] if "inactif" in ligne[2].lower()]
    
    if inactives:
        print(f"🔎 {len(inactives)} IA inactives détectées :")
        for ligne in inactives:
            print(f"— {ligne[0]} ({ligne[1]}, {ligne[3]})")
    else:
        print("✅ Aucune IA inactive détectée.")

def calculer_statistiques_profit():
    chemin_logs = "data/logs.csv"
    if not os.path.exists(chemin_logs):
        print("❌ Aucun journal trouvé pour calcul.")
        return {"total": 0, "inactives": 0, "actives": 0}

    with open(chemin_logs, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        lignes = list(reader)

    if len(lignes) <= 1:
        print("📭 Aucune donnée IA à analyser.")
        return {"total": 0, "inactives": 0, "actives": 0}

    total = len(lignes) - 1
    inactives = sum(1 for ligne in lignes[1:] if "inactif" in ligne[2].lower())
    actives = total - inactives

    print(f"📊 Total IA : {total}, Actives : {actives}, Inactives : {inactives}")
    return {"total": total, "inactives": inactives, "actives": actives}