import os
import ast

def summarize_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        tree = ast.parse(f.read(), filename=filepath)

    summary = {
        "file": os.path.basename(filepath),
        "classes": [],
        "functions": []
    }

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            summary["classes"].append(node.name)
        elif isinstance(node, ast.FunctionDef):
            summary["functions"].append(node.name)

    return summary

def summarize_project(directory):
    summaries = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                try:
                    summaries.append(summarize_file(path))
                except Exception as e:
                    print(f"⚠️ Erreur dans {file} : {e}")
    return summaries

def print_summary(summaries):
    print("\n📦 Résumé du projet 'bot_trading'")
    for s in summaries:
        print(f"\n📄 Fichier : {s['file']}")
        if s["classes"]:
            print("  🧠 Classes :")
            for c in s["classes"]:
                print(f"    - {c}")
        if s["functions"]:
            print("  ⚙️ Fonctions :")
            for f in s["functions"]:
                print(f"    - {f}")
        if not s["classes"] and not s["functions"]:
            print("  (aucune classe ou fonction détectée)")

if __name__ == "__main__":
    dossier_bot = "."  # ← pour scanner le dossier actuel
    resume = summarize_project(dossier_bot)
    print_summary(resume)