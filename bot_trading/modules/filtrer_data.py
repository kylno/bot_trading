import csv

fichier_entree = "data/exemple_data.csv"
fichier_sortie = "data/filtre_resultat.csv"
seuil_prix = 100.0  # Tu peux changer cette valeur selon ton test

try:
    print("🟢 Script lancé")
    lignes_filtrees = []

    with open(fichier_entree, "r", encoding="utf-8") as f_in:
        lecteur = csv.reader(f_in)
        entetes = next(lecteur)  # Lire l’en-tête

        print(f"\n🔍 Lignes avec prix ≥ {seuil_prix} :\n")
        print(f"{entetes[0]:<25} | {entetes[1]:>10}")
        print("-" * 40)

        for ligne in lecteur:
            try:
                prix = float(ligne[1])
                if prix >= seuil_prix:
                    lignes_filtrees.append(ligne)
                    print(f"{ligne[0]:<25} | {prix:>10.3f}")
            except ValueError:
                print(f"⚠️ Ligne ignorée (valeur invalide) : {ligne}")

    if lignes_filtrees:
        with open(fichier_sortie, "w", newline="", encoding="utf-8") as f_out:
            ecrivain = csv.writer(f_out)
            ecrivain.writerow(entetes)
            ecrivain.writerows(lignes_filtrees)
        print(f"\n✅ Données exportées dans : {fichier_sortie}")
    else:
        print("❕ Aucune ligne ne correspond au filtre.")

except FileNotFoundError:
    print(f"❌ Le fichier '{fichier_entree}' est introuvable.")
except Exception as e:
    print(f"⚠️ Erreur inattendue : {e}")