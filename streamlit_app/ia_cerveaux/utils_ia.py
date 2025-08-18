import pandas as pd
import streamlit as st

def charger_donnees(chemin_fichier: str) -> pd.DataFrame:
    """
    Charge un fichier CSV et retourne un DataFrame.
    
    Args:
        chemin_fichier (str): Chemin vers le fichier CSV.
    
    Returns:
        pd.DataFrame: Données chargées.
    """
    try:
        df = pd.read_csv(chemin_fichier)
        st.success(f"Données chargées depuis : {chemin_fichier}")
        return df
    except FileNotFoundError:
        st.error(f"Fichier introuvable : {chemin_fichier}")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"Erreur lors du chargement : {e}")
        return pd.DataFrame()

def apercu_donnees(df: pd.DataFrame, nb_lignes: int = 5) -> None:
    """
    Affiche un aperçu des données dans Streamlit.
    
    Args:
        df (pd.DataFrame): Le DataFrame à afficher.
        nb_lignes (int): Nombre de lignes à afficher.
    """
    if df.empty:
        st.warning("Aucune donnée à afficher.")
    else:
        st.subheader("Aperçu des données")
        st.dataframe(df.head(nb_lignes))
        st.write(f"Nombre de lignes : {len(df)}")
        st.write(f"Nombre de colonnes : {len(df.columns)}")