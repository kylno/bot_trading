import schedule
import time
import os
from datetime import datetime
from api.export import generer_pdf_du_jour  # tu peux adapter selon ton nom de fonction
from emailer import envoyer_email

DESTINATAIRE_PAR_DEFAUT = "klesournepro44@gmail.com"

def job():
    date_du_jour = datetime.now().strftime("%Y-%m-%d")
    fichier = f"exports/rapport_{date_du_jour}.pdf"

    if os.path.exists(fichier):
        print(f"📎 Rapport déjà généré aujourd’hui ({date_du_jour})")
    else:
        print(f"🧠 Génération du rapport du {date_du_jour}...")
        generer_pdf_du_jour()  # 🛠️ fonction à adapter depuis ton export.py

    print("📤 Envoi de l’e-mail...")
    try:
        envoyer_email(DESTINATAIRE_PAR_DEFAUT)
    except Exception as e:
        print(f"⚠️ Erreur d’envoi : {e}")
        return
    print("✅ Rapport envoyé avec succès à", DESTINATAIRE_PAR_DEFAUT)

def main():
    # Horaire automatisé (modifiable ici)
    schedule.every().day.at("14:50").do(job)

    print("⏳ Planificateur IA prêt. Envoi prévu chaque jour à 14h50.")
    while True:
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()