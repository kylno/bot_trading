import csv

fichier = "data/exemple_data.csv"

try:
    with open(fichier, "r", encoding="utf-8") as f:
        lecteur = csv.reader(f)
        entetes = next(lecteur)  # Lire l’en-tête

        print(f"\n🗂️ Données extraites depuis {fichier} :\n")
        print(f"{entetes[0]:<25} | {entetes[1]:>10}")
        print("-" * 40)

        for ligne in lecteur:
            print(f"{ligne[0]:<25} | {ligne[1]:>10}")

except FileNotFoundError:
    print(f"❌ Le fichier '{fichier}' est introuvable.")
except Exception as e:
    print(f"⚠️ Erreur : {e}")