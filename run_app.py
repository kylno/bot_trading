import os
import subprocess
import sys

def check_env():
    """
    Vérifie que Streamlit est installé, sinon propose l'installation.
    """
    try:
        import streamlit
    except ImportError:
        print("⚠️ Streamlit n'est pas installé. Installation...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit"])


def launch_dashboard():
    """
    Lance l'application Streamlit du cockpit IA.
    """
    path_to_app = "streamlit_app/dashboard.py"
    
    if not os.path.exists(path_to_app):
        print(f"❌ Fichier introuvable : {path_to_app}")
        return

    print("🚀 Démarrage du Cockpit IA...")
    subprocess.call(["streamlit", "run", path_to_app])


if __name__ == "__main__":
    print("🧠 Préparation de l’environnement IA")
    check_env()
    launch_dashboard()