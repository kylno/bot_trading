# 🤖 Liaison entre actifs et bots
ACTIF_BOT = {
    "bitcoin": "Berzerk+",
    "eth": "Shadow",
    "solana": "Fourmi",
    "apple": "Casa de Papel",
    "nasdaq": "Casa de Papel",
    "gold": "GoldHunter"
}

def get_bot_for_actif(actif):
    """
    Retourne le nom du bot associé à un actif donné.
    """
    return ACTIF_BOT.get(actif.lower(), None)

def get_all_bindings():
    """
    Retourne toutes les liaisons bot ↔ actif.
    """
    return ACTIF_BOT