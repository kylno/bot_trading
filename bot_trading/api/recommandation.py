from graph_profit import get_stats

def get_recommandation():
    stats = get_stats()

    # Détecte stratégie avec le meilleur profit moyen
    meilleure_strategie = max(stats["strategies"], key=lambda s: s[1], default=["Aucune", 0])
    # Détecte crypto avec le profit total le plus élevé
    meilleur_symbole = max(stats["symboles"], key=lambda s: s[1], default=["Aucun", 0])
    # Taux de réussite global
    taux_reussite = 100 * stats["gagnants"] / stats["total"] if stats["total"] else 0

    # Assemble la recommandation
    return {
        "strategie": meilleure_strategie[0],
        "symbole": meilleur_symbole[0],
        "taux": f"{taux_reussite:.1f}%",
        "suggestion": f"🧠 Essayez {meilleure_strategie[0]} sur {meilleur_symbole[0]}"
    }