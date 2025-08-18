import importlib.util
import socket
import os

# 📋 Liste des modules requis pour BrainTrader-XI
MODULES_REQUIS = [
    "streamlit",
    "pandas",
    "altair",
    "requests",
    "schedule"
]

# 🌍 Connexions API à tester
API_CIBLES = {
    "CoinGecko": "api.coingecko.com",
    "Telegram": "api.telegram.org"
}

def verifier_modules(modules):
    manquants = []
    print("🧪 Vérification des modules Python requis :\n")
    for mod in modules:
        if importlib.util.find_spec(mod) is not None:
            print(f"✅ {mod}")
        else:
            print(f"❌ {mod} absent")
            manquants.append(mod)
    return manquants

def test_connexion(hote, port=443):
    try:
        socket.create_connection((hote, port), timeout=3)
        return True
    except:
        return False

def verifier_api(cibles):
    print("\n🌐 Test des connexions API :\n")
    for nom, hote in cibles.items():
        etat = test_connexion(hote)
        emoji = "✅" if etat else "❌"
        print(f"{emoji} Connexion à {nom} ({hote})")

def suggestion_install(modules):
    if modules:
        print("\n📦 Modules manquants :")
        print("➡️ Exécute cette commande pour les installer :")
        print(f"pip install {' '.join(modules)}")
    else:
        print("\n🚀 Tous les modules sont présents 🎯")

if __name__ == "__main__":
    print("🔎 Diagnostic de l’environnement BrainTrader-XI\n")
    manquants = verifier_modules(MODULES_REQUIS)
    verifier_api(API_CIBLES)
    suggestion_install(manquants)