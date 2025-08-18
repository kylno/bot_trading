import os
import shutil
import sys

structure = {
    "bots": ["realtime_berserk.py", "discord_bot.py", "discord_switch.py"],
    "modules": ["filtrer_data.py", "generateur.py", "grapher.py", "executor.py", "missions.py", "emailer.py"],
    "config": ["config_email.json", "config_mode.json", "settings.json", "requirements.txt"],
    "core": ["menu.py", "dashboard.py"],
    "tools": ["install_module.bat", "lancer_cockpit.bat", "lancer_dashboard.bat"],
    "frontend/static/images": ["fond.png"]
}

def find_file(filename):
    for root, _, files in os.walk("."):
        if filename in files:
            return os.path.join(root, filename)
    return None

def organiser_projet(dry_run=False):
    print("\n📦 Organisation du cockpit IA — mode simulation :", "ON" if dry_run else "OFF", "\n")
    total = 0
    log_entries = []

    for dossier_cible, fichiers in structure.items():
        os.makedirs(dossier_cible, exist_ok=True)
        for fichier in fichiers:
            chemin_actuel = find_file(fichier)
            chemin_destination = os.path.join(dossier_cible, fichier)

            if chemin_actuel:
                if dry_run:
                    print(f"🔍 Simulation : {fichier} serait déplacé → {dossier_cible}/")
                    log_entries.append(f"SIMULATION : {fichier} → {dossier_cible}/")
                else:
                    try:
                        shutil.move(chemin_actuel, chemin_destination)
                        print(f"✅ Déplacé : {fichier} → {dossier_cible}/")
                        log_entries.append(f"DÉPLACÉ : {fichier} → {dossier_cible}/")
                        total += 1
                    except Exception as e:
                        print(f"⚠️ Erreur : {fichier} → {e}")
            else:
                print(f"❌ Introuvable : {fichier} — ignoré")
                log_entries.append(f"IGNORÉ : {fichier}")

    with open("organiseur_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write("\n--- SESSION ---\n")
        for entry in log_entries:
            log_file.write(entry + "\n")

    print(f"\n📊 Résumé : {total} fichier(s) déplacé(s)")
    print("🧠 Log enregistré dans 'organiseur_log.txt'")
    print("🎯 Organisation terminée ! Ton cockpit IA est calibré pour le décollage 🚀\n")

if __name__ == "__main__":
    simulate = "--simulate" in sys.argv
    organiser_projet(dry_run=simulate)