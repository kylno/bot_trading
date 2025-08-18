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

        for mot in mots_positifs:
            if mot in texte:
                score += 10

        for mot in mots_negatifs:
            if mot in texte:
                score -= 10

        score += source_bonus.get(source, 0)
        a["score"] = max(0, min(100, score))

    return alertes


def choisir_meilleur_actif():
    """
    Sélectionne l’actif avec le meilleur score parmi les alertes disponibles.
    Retourne le symbole de l’actif ou None si aucun score suffisant.
    """
    alertes = [
        {"symbole": "BTCUSDT", "texte": "Massive breakout incoming 🚀", "source": "X"},
        {"symbole": "ETHUSDT", "texte": "Bearish divergence spotted", "source": "Telegram"},
        {"symbole": "SOLUSDT", "texte": "Pump confirmed by whales", "source": "Discord"},
        {"symbole": "XRPUSDT", "texte": "Possible dump after fake rally", "source": "News"}
    ]

    alertes_scored = scorer_alertes(alertes)
    alertes_scored.sort(key=lambda x: x["score"], reverse=True)

    meilleur = alertes_scored[0]
    if meilleur["score"] >= 60:
        return meilleur["symbole"]
    else:
        return None