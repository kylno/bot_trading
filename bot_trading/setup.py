import os

folders = ["logs", "config", "core", "streamlit_app"]
files = {
    "config/config_ia.json": '{"vacances": false}',
    "logs/capital.jsonl": "",
    "logs/investissements.json": "{}"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Dossiers et fichiers initiaux créés.")