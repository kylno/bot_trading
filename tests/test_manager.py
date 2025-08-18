from core.collecteurs_alertes import collecter_alertes
from core.scoring_alertes import scorer_alertes
from core.triggers_bot import détecter_et_déclencher
from core.historique_reco import enregistrer_reco

def test_collecte():
    print("🔍 Test collecte d’alertes...")
    alertes = collecter_alertes()
    assert isinstance(alertes, list), "La collecte doit retourner une liste"
    print(f"✅ {len(alertes)} alertes collectées")

def test_scoring():
    print("🧠 Test scoring des alertes...")
    alertes = collecter_alertes()
    scored = scorer_alertes(alertes)
    assert all("score" in a for a in scored), "Chaque alerte doit avoir un score"
    print(f"✅ {len(scored)} alertes scorées")

def test_trigger():
    print("🚀 Test déclenchement des bots...")
    alertes = [
        {"texte": "Bitcoin pump confirmé", "score": 95, "source": "X"},
        {"texte": "Apple chute brutale", "score": 92, "source": "News"}
    ]
    détecter_et_déclencher(alertes)
    print("✅ Déclenchement simulé terminé")

def test_historique():
    print("📜 Test enregistrement historique...")
    enregistrer_reco(
        bot="Berzerk+",
        actif="Bitcoin",
        score=93,
        raison="Test manuel",
        action="Simulation"
    )
    print("✅ Recommandation enregistrée")

if __name__ == "__main__":
    test_collecte()
    test_scoring()
    test_trigger()
    test_historique()