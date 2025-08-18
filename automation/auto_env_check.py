import os
import sys
import importlib
from datetime import datetime

def log(message):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def check_file(path):
    if os.path.exists(path):
        log(f"✅ Fichier trouvé : {path}")
    else:
        log(f"❌ Fichier manquant : {path}")

def check_package(pkg_name):
    try:
        importlib.import_module(pkg_name)
        log(f"✅ Package installé : {pkg_name}")
    except ImportError:
        log(f"❌ Package manquant : {pkg_name}")

def run_diagnostic():
    log("🔍 Démarrage du diagnostic IA\n")

    # 📁 Fichiers critiques à vérifier
    log("📂 Vérification des fichiers essentiels :")
    check_file("logs/profit_log.csv")
    check_file("streamlit_app/centre_de_mission.py")
    check_file("streamlit_app/style.css")
    check_file("streamlit_app/pages/statistiques_ia.py")
    check_file("streamlit_app/images/checklist.gif")
    print()

    # 🧪 Packages Python à tester
    log("📦 Vérification des packages Python :")
    check_package("streamlit")
    check_package("pandas")
    check_package("numpy")
    check_package("matplotlib")
    print()

    # ✅ Diagnostic terminé
    log("✅ Diagnostic terminé avec succès.")

if __name__ == "__main__":
    run_diagnostic()