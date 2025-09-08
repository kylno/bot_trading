class MicroCap1IA:
    def __init__(self):
        self.nom = "MicroCap1"
        self.strategie = "exploitation_hausses_moyennes"
        self.seuil_min = 0.5  # 50%
        self.seuil_max = 1.0  # 100%

    def analyser(self, donnees):
        variations = donnees.get("variations", [])
        signaux = [v for v in variations if self.seuil_min <= v <= self.seuil_max]
        signal = bool(signaux)
        confiance = round(len(signaux) / max(len(variations), 1), 2)
        return {
            "signal": signal,
            "confiance": confiance,
            "strategie": self.strategie
        }

    def afficher_resume(self):
        print(f"[{self.nom}] Stratégie : {self.strategie}")
        print(f"Seuils : {self.seuil_min*100}% à {self.seuil_max*100}%")