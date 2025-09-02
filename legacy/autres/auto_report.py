from core.rapport_pdf import generer_rapport_pdf
from core.telegram_bot import envoyer_rapport_telegram

# Générer le rapport PDF
if generer_rapport_pdf():
    print("✅ Rapport PDF généré.")
    # Envoyer sur Telegram
    if envoyer_rapport_telegram("TON_BOT_TOKEN", "TON_CHAT_ID"):
        print("📤 Rapport envoyé sur Telegram.")
    else:
        print("❌ Échec de l'envoi Telegram.")
else:
    print("❌ Échec de la génération du rapport.")