import pandas as pd

def charger_donnees(path):
    try:
        return pd.read_csv(path)
    except Exception as e:
        print(f"Erreur chargement: {e}")
        return None