import smtplib
import ssl
import json
import os
from email.message import EmailMessage
from datetime import datetime

def charger_config():
    with open("config_mail.json", "r", encoding="utf-8") as f:
        return json.load(f)

def envoyer_email(destinataire):
    config = charger_config()
    expediteur = config["email"]
    mot_de_passe = config["mot_de_passe"]
    smtp = config["smtp"]
    port = config["port"]

    # PDF du jour
    date_du_jour = datetime.now().strftime("%Y-%m-%d")
    fichier_pdf = f"exports/rapport_{date_du_jour}.pdf"

    if not os.path.exists(fichier_pdf):
        print(f"❌ PDF introuvable : {fichier_pdf}")
        return

    # Création du mail
    msg = EmailMessage()
    msg["Subject"] = f"Rapport IA - BrainTrader-X1 ({date_du_jour})"
    msg["From"] = expediteur
    msg["To"] = destinataire

    # Contenu HTML + texte alternatif
    msg.set_content("Veuillez trouver ci-joint le rapport IA du jour.", subtype="plain")
    msg.add_alternative(f"""\
    <html>
      <body style="font-family: Arial, sans-serif; color: #222; font-size: 15px;">
        <p>Bonjour,</p>
        <p>Veuillez trouver ci-joint le rapport PDF généré automatiquement ce jour par votre cockpit IA <strong>BrainTrader-X1</strong>.</p>
        <p>Il contient les dernières missions, statistiques et visualisations IA.</p>
        <p>Cordialement,<br>— Le noyau d’analyse de <strong>BrainTrader-X1</strong></p>

        <hr style="margin-top: 40px; border: none; border-top: 1px solid #ccc;">

        <table style="margin-top: 20px; font-family: Arial, sans-serif; font-size: 14px;">
          <tr>
            <td style="padding-right: 15px;">
              <img src="https://i.imgur.com/WUI2Nru.png" alt="Avatar IA" width="60" style="border-radius: 50%;">
            </td>
            <td>
              <strong>BrainTrader-X1</strong><br>
              Noyau analytique IA autonome<br>
              <span style="color: #666;">Capitaine : Kylian</span><br>
              <a href="mailto:braintrader@ai.labs" style="color: #888;">braintrader@ai.labs</a>
            </td>
          </tr>
        </table>
      </body>
    </html>
    """, subtype="html")

    # Ajout de la pièce jointe PDF
    with open(fichier_pdf, "rb") as f:
        data = f.read()
        nom = os.path.basename(fichier_pdf)
        msg.add_attachment(data, maintype="application", subtype="pdf", filename=nom)

    # Envoi SMTP
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp, port, context=context) as server:
            server.login(expediteur, mot_de_passe)
            server.send_message(msg)
        print(f"✅ E-mail envoyé à {destinataire}")
    except Exception as e:
        print(f"⚠️ Échec de l’envoi : {e}")