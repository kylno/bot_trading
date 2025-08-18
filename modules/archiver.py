import os
import re
import shutil

def archiver_rapports():
    dossier_base = "exports/"
    fichiers = os.listdir(dossier_base)

    pattern_pdf = r"rapport_(\d{4})-(\d{2})-(\d{2})\.pdf"
    pattern_graph = r"graphique_missions.png"

    for fichier in fichiers:
        chemin_fichier = os.path.join(dossier_base, fichier)

        # Déplacement des PDF de rapport
        match = re.match(pattern_pdf, fichier)
        if match and os.path.isfile(chemin_fichier):
            annee, mois, _ = match.groups()
            dossier_cible = os.path.join(dossier_base, annee, mois)
            os.makedirs(dossier_cible, exist_ok=True)

            shutil.move(chemin_fichier, os.path.join(dossier_cible, fichier))
            print(f"📁 {fichier} déplacé vers {dossier_cible}/")

            # S’il existe un graphique générique : on le déplace aussi avec le PDF
            chemin_graph = os.path.join(dossier_base, "graphique_missions.png")
            if os.path.exists(chemin_graph):
                nouveau_nom = f"graphique_{annee}-{mois}.png"
                shutil.move(chemin_graph, os.path.join(dossier_cible, nouveau_nom))
                print(f"🖼️ Graphique déplacé et renommé : {nouveau_nom}")

if __name__ == "__main__":
    archiver_rapports()