import os

# 📦 Structure attendue du cockpit IA
structure_attendue = {
    "automation": ["auto_env_check.py"],
    "logs": ["profit_log.csv", "diagnostic_log.csv"],
    "streamlit_app": [
        "style.css",
        "centre_de_mission.py"
    ],
    "streamlit_app/images": [
        "checklist.gif",
        "intro_cockpit.gif",
        "security.gif"
    ],
    "streamlit_app/pages": [
        "statistiques_ia.py",
        "diagnostic_ia.py",
        "pilotage_ia.py"
    ],
    ".": ["main.py", "menu.py"]
}

def verifier():
    print("🔍 Vérification de la structure IA...\n")
    tout_est_bon = True

    for dossier, fichiers in structure_attendue.items():
        for fichier in fichiers:
            chemin = os.path.join(dossier, fichier)
            if os.path.exists(chemin):
                print(f"✅ {chemin}")
            else:
                print(f"❌ {chemin} manquant")
                tout_est_bon = False

    if tout_est_bon:
        print("\n✅ Structure complète et conforme")
    else:
        print("\n🚨 Structure partiellement incorrecte")

if __name__ == "__main__":
    verifier()