import os
from datetime import datetime

from missions import generer_mission_auto, generer_missions_multiples
from modules.stats import (
    simuler_colonie,
    generer_nom_ia_stylise,
    detecter_ia_inactives
)
from api.export import export_statut_pdf
from modules.graphiques import generer_graphiques

def menu():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Générer une mission IA")
        print("2. Générer plusieurs missions IA")
        print("3. Simuler un cycle de colonie IA")
        print("4. Générer un nom IA stylisé")
        print("5. Détecter les IA inactives")
        print("6. Générer graphique des missions")
        print("7. Exporter statut PDF")
        print("8. Envoyer PDF par e-mail")
        print("9. Ouvrir le rapport PDF")
        print("10. Lancer l'interface graphique")
        print("11. Ouvrir le dossier des rapports PDF")
        print("12. Voir les 3 derniers rapports générés")
        print("q. Quitter le cockpit")
        choix = input("👉 Ton choix : ")

        if choix == "1":
            generer_mission_auto()
        elif choix == "2":
            generer_missions_multiples()
        elif choix == "3":
            simuler_colonie()
        elif choix == "4":
            generer_nom_ia_stylise()
        elif choix == "5":
            detecter_ia_inactives()
        elif choix == "6":
            generer_graphiques()
        elif choix == "7":
            export_statut_pdf()
        elif choix == "8":
            print("📧 Envoi par e-mail pas encore implémenté.")
        elif choix == "9":
            date_du_jour = datetime.now().strftime("%Y-%m-%d")
            chemin_pdf = f"exports/rapport_{date_du_jour}.pdf"
            if os.path.exists(chemin_pdf):
                os.startfile(chemin_pdf)
                print(f"📂 Ouverture de : {chemin_pdf}")
            else:
                print(f"⚠️ Aucun rapport PDF trouvé pour aujourd'hui : {chemin_pdf}")
        elif choix == "10":
            print("🖥️ Interface graphique pas encore codée.")
        elif choix == "11":
            try:
                os.startfile("exports")
                print("📁 Dossier 'exports/' ouvert dans l’explorateur.")
            except Exception as e:
                print(f"⚠️ Impossible d’ouvrir le dossier : {e}")
        elif choix == "12":
            try:
                fichiers = sorted(
                    [f for f in os.listdir("exports") if f.endswith(".pdf")],
                    reverse=True
                )
                derniers = fichiers[:3]
                if derniers:
                    print("\n🗂️ 3 derniers rapports PDF :")
                    for f in derniers:
                        print("📄", f)
                else:
                    print("📭 Aucun rapport PDF disponible.")
            except Exception as e:
                print(f"⚠️ Erreur en lisant les fichiers PDF : {e}")
        elif choix.lower() == "q":
            print("👋 À bientôt, capitaine !")
            break
        else:
            print("❓ Option inconnue. Réessaye.")