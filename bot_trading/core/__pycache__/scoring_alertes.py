def scorer_alertes(alertes):
    """
    Analyse chaque alerte et attribue un score entre 0 et 100
    basé sur la présence de mots-clés haussiers ou baissiers.
    """
    mots_positifs = ["pump", "breakout", "bullish", "buy", "explose", "moon", "rally"]
    mots_negatifs = ["crash", "bearish", "sell", "drawdown", "liquidation", "dump", "panic"]

    source_bonus = {
        "X": 5,
        "Discord": 3,
        "Telegram": 2,
        "News": 4
    }

    for a in alertes:
        texte = a.get("texte", "").lower()
        source = a.get("source", "")
        score = 50  # Score neutre de base

        # 🔼 Ajout de points pour les mots positifs
        for mot in mots_positifs:
            if mot in texte:
                score += 10

        # 🔽 Retrait de points pour les mots négatifs
        for mot in mots_negatifs:
            if mot in texte:
                score -= 10

        # 🎯 Bonus selon la source
        score += source_bonus.get(source, 0)

        # 🧠 Clamp le score entre 0 et 100
        a["score"] = max(0, min(100, score))

    return alertes