def lire_requirements(fichier="requirements.txt"):
    try:
        with open(fichier, "r", encoding="utf-8") as f:
            lignes = [l.strip() for l in f.readlines() if l.strip() and not l.startswith("#")]
            return lignes
    except FileNotFoundError:
        return []

def verifier_modules():
    import importlib.util
    modules = lire_requirements()
    etat = {}
    for m in modules:
        nom = m.split("==")[0].strip()
        etat[nom] = importlib.util.find_spec(nom) is not None
    return etat