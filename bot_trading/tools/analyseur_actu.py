# analyseur_actus.py

# 🔎 Liste d'actifs financiers à reconnaître
actifs_connus = [
    "BTC", "ETH", "SOL", "DOGE", "ADA", "XRP", "BNB", "TSLA", "AAPL", "AMZN"
]

# 💥 Mots typiques de hype (souvent peu fiables)
mots_hype = [
    "to the moon", "100x", "explose", "buzz", "buy now", "pump", "rocket", "rich", "moon", "all-in"
]

# 📊 Mots indiquant une info sérieuse / structurée
mots_serieux = [
    "SEC", "procès", "audit", "partenariat", "investisseur institutionnel", "résultats", "analyse technique", "on-chain", "fondamental"
]

def analyser_message(message):
    """Analyse un message et retourne score crédibilité, actifs et niveau"""
    message_min = message.lower()
    actifs_detectés = [a for a in actifs_connus if a.lower() in message_min]

    score = 0
    if any(mot in message_min for mot in mots_hype):
        score -= 1
    if any(mot in message_min for mot in mots_serieux):
        score += 2
    if "sec" in message_min or "justice" in message_min:
        score += 1
    if len(message.split()) >= 10:
        score += 1

    if score >= 3:
        niveau = "✅ Signal crédible"
    elif score == 2:
        niveau = "🟡 À surveiller"
    else:
        niveau = "❌ Probable bluff ou bruit"

    return {
        "message": message,
        "actifs": actifs_detectés if actifs_detectés else ["aucun"],
        "score": score,
        "niveau": niveau
    }

# 📌 Exemple de test (exécuté si tu lances ce fichier directement)
if __name__ == "__main__":
    exemples = [
        "BTC va to the moon ce soir, préparez-vous !!!",
        "La SEC attaque Binance, grosse turbulence probable",
        "Mon cousin dit que DOGE va x100, foncez !",
        "Tesla annonce un partenariat stratégique en Asie"
    ]

    for texte in exemples:
        print(f"\n📝 {texte}")
        resultat = analyser_message(texte)
        print(f"🔍 Actifs : {resultat['actifs']}")
        print(f"🎯 Score : {resultat['score']}/5")
        print(f"⚖️ Niveau : {resultat['niveau']}")