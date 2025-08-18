# dispatch/fourmi_dispatcher.py

import csv
from datetime import datetime

# 📦 État actuel de la fourmilière
fourmis = {
    "fourmi_01": "disponible",
    "fourmi_02": "disponible",
    "fourmi_03": "disponible",
    "fourmi_04": "disponible"
}

# 🧮 Compteur de missions
missions = {
    "fourmi_01": 0,
    "fourmi_02": 0,
    "fourmi_03": 0,
    "fourmi_04": 0
}

# 🎭 Historique des rôles par fourmi
roles_historique = {
    "fourmi_01": [],
    "fourmi_02": [],
    "fourmi_03": [],
    "fourmi_04": []
}

# 📋 Journal des missions dans logs/fourmi_log.csv
def log_mission(nom, role, bot_cible):
    try:
        with open("logs/fourmi_log.csv", mode="a", newline="", encoding="utf-8") as fichier:
            writer = csv.writer(fichier)
            writer.writerow([
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                nom,
                role,
                bot_cible
            ])
    except Exception as e:
        print(f"⚠️ Erreur lors de l’écriture du log : {e}")

# 🐜 Assignation d'une fourmi disponible à une mission
def assigner_fourmi(role, bot_cible):
    for nom, etat in fourmis.items():
        if etat == "disponible":
            fourmis[nom] = role
            missions[nom] += 1
            roles_historique[nom].append(role)
            log_mission(nom, role, bot_cible)
            print(f"✅ {nom} assignée à {bot_cible} pour mission : {role}")
            return nom
    print("❌ Aucune fourmi disponible pour cette mission.")
    return None

# 🧹 Libération d'une fourmi (la remet disponible)
def liberer_fourmi(nom):
    if nom in fourmis:
        fourmis[nom] = "disponible"
        print(f"🛑 {nom} libérée et de nouveau disponible.")

# 🧠 Affichage du statut global de la fourmilière
def afficher_statut():
    print("\n📊 État de la fourmilière :")
    for nom in fourmis:
        etat = fourmis[nom]
        total = missions[nom]
        derniers_roles = ", ".join(roles_historique[nom][-3:]) if roles_historique[nom] else "Aucun"
        print(f"- {nom} → {etat} | Missions : {total} | Derniers rôles : {derniers_roles}")