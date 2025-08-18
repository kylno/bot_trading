import os

structure = {
    "api": {"app.py": "# API Flask (à compléter)"},
    "bots": {
        "fourmi_bot.py": "def run_fourmi_bot(c): print(f'🐜 Fourmi: {c}€')",
        "berserk_bot.py": "def run_berserk_bot(c): print(f'⚔️ Berserk: {c}€')",
        "shadow_bot.py": "def run_shadow_bot(c): print(f'👁 Shadow: {c}€')"
    },
    "core": {"manager.py": "from bots.fourmi_bot import *\nfrom bots.berserk_bot import *\nfrom bots.shadow_bot import *\nfrom config import *\n\ndef run_all_bots():\n    run_fourmi_bot(CAPITAL_INITIAL * ALLOCATION['fourmi'])\n    run_berserk_bot(CAPITAL_INITIAL * ALLOCATION['berserk'])\n    run_shadow_bot(CAPITAL_INITIAL * ALLOCATION['shadow'])"},
    "engine": {
        "volatility.cpp": "// C++ moteur haute perf (à compléter)",
        "compile.bat": "g++ -shared -o volatility.dll -fPIC volatility.cpp"
    },
    "utils": {"bindings.py": "# Liaison Python ↔ C++"},
    "logs": {"trades.log": ""},
    "data": {"exemple_data.csv": "timestamp,price\n0,123"},
    ".": {
        "main.py": "from core.manager import run_all_bots\nif __name__ == '__main__': run_all_bots()",
        "config.py": "CAPITAL_INITIAL = 1000\nALLOCATION = { 'fourmi': 0.6, 'berserk': 0.3, 'shadow': 0.1 }",
        "requirements.txt": "flask",
        "README.md": "# BOT_INFRASTRUCTURE\nInfrastructure de trading algorithmique Python/C++"
    }
}

def create_structure(base, tree):
    for name, content in tree.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    create_structure(".", structure)
    print("✅ Projet généré avec succès dans le dossier actuel.")