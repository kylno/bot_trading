import os
import re
import importlib.util
from pathlib import Path
from datetime import datetime

DOSSIER_CERVEAUX = "streamlit_app/ia_cerveaux"
DOSSIER_LOGS = "streamlit_app/outils/logs"
DATE_HORAIRE = datetime.now().strftime("%Y%m%d_%H%M%S")
RAPPORT_PATH = f"{DOSSIER_LOGS}/rapport_scan_IA_{DATE_HORAIRE}.txt"

# Création du dossier de logs s'il n'existe pas
os.makedirs(DOSSIER_LOGS, exist_ok=True)

def extraire_classes(chemin):
    """Retourne toutes les définitions de classes présentes dans un fichier .py"""
    try:
        with open(chemin, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            return re.findall(r'class\s+(\w+)', contenu)
    except Exception as e:
        return []

def charger_classe(module_path, class_name):
    """Importe dynamiquement une classe depuis son fichier"""
    spec = importlib.util.spec_from_file_location("module", module_path)
    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
        return getattr(module, class_name)
    except Exception as e:
        return None

def scanner_dossier():
    rapport = []
    print("🧠 Scan des cerveaux IA...\n")
    
    for fichier in os.listdir(DOSSIER_CERVEAUX):
        if fichier.endswith(".py"):
            chemin_fichier = os.path.join(DOSSIER_CERVEAUX, fichier)
            classes_trouvees = extraire_classes(chemin_fichier)
            
            if classes_trouvees:
                for nom in classes_trouvees:
                    cls = charger_classe(chemin_fichier, nom)
                    if cls:
                        try:
                            instance = cls()
                            if callable(getattr(instance, "conseiller", None)):
                                conseil = instance.conseiller()
                                ligne = f"✅ {fichier} → {nom}: {conseil}"
                                print(ligne)
                                rapport.append(ligne)
                            else:
                                ligne = f"⚠️ {fichier} → {nom} sans méthode conseiller()"
                                print(ligne)
                                rapport.append(ligne)
                        except Exception as e:
                            ligne = f"⚠️ {fichier} → {nom} erreur lors de l'exécution: {e}"
                            print(ligne)
                            rapport.append(ligne)
                    else:
                        ligne = f"❌ {fichier} → impossible d’importer la classe {nom}"
                        print(ligne)
                        rapport.append(ligne)
            else:
                ligne = f"❌ {fichier} → aucune classe détectée"
                print(ligne)
                rapport.append(ligne)

    with open(RAPPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(rapport))
    
    print(f"\n📄 Rapport enregistré dans {RAPPORT_PATH}")

scanner_dossier()