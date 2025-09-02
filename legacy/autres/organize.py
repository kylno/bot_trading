import os
import shutil

ROOT_DIR = r"C:\Users\kleso\OneDrive\Desktop\bot_trading"

structure = {
    "api": ["__init__.py", "api_user.py", "db.py", "export.py", "run.bat"],
    "api/config": [],

    "automation/auto_env": [],
    "automation/bot": [],
    "automation/bot_trading": ["bot_loader.py", "universal_price.py", "scoring_alert.py"],

    "ia": ["diagnostic_ia.py", "scanner_ai.py", "utils_ia.py"],

    "interface": ["dashboard.py"],
    "interface/streamlit_app": [],
    "interface/templates": [],

    "data": ["capital.json", "exemple_data.csv", "filtre_resultat.csv"],
    "data/logs": [],

    "config": ["ia.json", "settings.json"],
    "config/config_mod": [],

    "tools": [
        "collector_alert.py", "crypto_scanner.py", "datagenerator.py",
        "historique_reco.py", "report_pdf.py", "security_watchdog.py", "stat_comparatif.py"
    ],

    "telegram": ["telegram_bot.py"],

    "tests/test_api": [],
    "tests/test_ia": [],

    "docs": ["README.md", "roadmap.md", "architecture.md"],

    "legacy/core_copie": [],
    "legacy/config_copie": [],
    "legacy/autres": []
}

def organize_files():
    moved_files = set()
    for folder, files in structure.items():
        folder_path = os.path.join(ROOT_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            src = os.path.join(ROOT_DIR, file)
            dst = os.path.join(folder_path, file)

            if os.path.exists(src):
                shutil.move(src, dst)
                moved_files.add(file)
                print(f"✅ Déplacé : {file} → {folder}")

    return moved_files

def detect_unlisted_files(moved_files):
    all_files = [f for f in os.listdir(ROOT_DIR) if os.path.isfile(os.path.join(ROOT_DIR, f))]
    unlisted = [f for f in all_files if f not in moved_files]
    return unlisted

def archive_unlisted_files(unlisted):
    archive_path = os.path.join(ROOT_DIR, "legacy", "autres")
    os.makedirs(archive_path, exist_ok=True)

    for file in unlisted:
        src = os.path.join(ROOT_DIR, file)
        dst = os.path.join(archive_path, file)
        shutil.move(src, dst)
        print(f"📦 Archivé : {file} → legacy/autres")

def generate_readme():
    readme_path = os.path.join(ROOT_DIR, "docs", "README.md")
    os.makedirs(os.path.dirname(readme_path), exist_ok=True)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# 📦 Projet Bot Trading\n\n")
        f.write("Ce projet est structuré pour gérer un bot de trading automatisé avec des modules d'IA, des interfaces utilisateur, des scripts d'automatisation et des outils d'analyse.\n\n")
        f.write("## 📁 Structure\n")
        for folder in structure:
            f.write(f"- `{folder}/`\n")
        f.write("\n## 🚀 Lancement\n")
        f.write("Utilisez `python organize.py` pour ranger automatiquement le projet.\n")
        f.write("\n## 🧠 Modules clés\n")
        f.write("- **API** : endpoints, base de données\n")
        f.write("- **Automation** : routines et bots\n")
        f.write("- **IA** : diagnostic et analyse\n")
        f.write("- **Interface** : Streamlit et dashboard\n")
        f.write("- **Data** : fichiers CSV et JSON\n")
        f.write("- **Tools** : scripts utilitaires\n")
        f.write("- **Telegram** : intégration bot\n")
        f.write("- **Tests** : tests unitaires\n")
        f.write("- **Legacy** : archives et copies\n")

    print("📝 README.md généré dans docs/")

if __name__ == "__main__":
    print("📂 Organisation du projet en cours...\n")
    moved = organize_files()
    unlisted = detect_unlisted_files(moved)
    if unlisted:
        print("\n🔍 Fichiers non listés détectés :")
        for f in unlisted:
            print(f" - {f}")
        archive_unlisted_files(unlisted)
    else:
        print("\n✅ Aucun fichier non listé détecté.")

    generate_readme()
    print("\n🎉 Projet entièrement rangé et documenté !")