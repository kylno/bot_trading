import os
import pandas as pd
import streamlit as st
from datetime import datetime

# -----------------------------
# CONFIG
# -----------------------------
DATA_DIR = "graphs"
CAPITAL_CSV = os.path.join(DATA_DIR, "courbe_capital.csv")

# -----------------------------
# FONCTIONS
# -----------------------------
@st.cache_data(show_spinner=False)
def load_capital_curve(path=CAPITAL_CSV):
    """Charge la courbe du capital depuis un CSV, ou renvoie un fallback."""
    if os.path.exists(path):
        try:
            df = pd.read_csv(path)
            if "date" in df.columns and "capital" in df.columns:
                df["date"] = pd.to_datetime(df["date"])
                return df.sort_values("date")
        except Exception as e:
            st.error(f"Erreur lecture CSV: {e}")

    # fallback minimal si pas de fichier
    return pd.DataFrame({
        "date": pd.to_datetime([datetime(2025, 1, 1)]),
        "capital": [10000.0],
    })


def append_capital_value(value, when=None, path=CAPITAL_CSV):
    """Ajoute une nouvelle valeur de capital dans le CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    when = when or datetime.utcnow()
    row = pd.DataFrame([{"date": when, "capital": float(value)}])

    if os.path.exists(path):
        row.to_csv(path, mode="a", header=False, index=False)
    else:
        row.to_csv(path, index=False)

# Exemple : appelle `append_capital_value(capital_actuel)` dans ton moteur


# -----------------------------
# UI STREAMLIT
# -----------------------------
st.set_page_config(page_title="Courbe du capital", layout="wide")

st.title("📈 Courbe du capital")

# Charger la donnée
df_cap = load_capital_curve()

# Choix d’affichage
mode = st.radio("Échelle", ["Linéaire", "Log"], horizontal=True)

if mode == "Log":
    # éviter les zéros/négatifs en log
    df_plot = df_cap.copy()
    df_plot["capital_log"] = df_plot["capital"].apply(lambda x: max(x, 1))
    st.line_chart(df_plot.set_index("date")[["capital_log"]])
else:
    st.line_chart(df_cap.set_index("date")[["capital"]])

# Bouton pour ajouter une valeur de capital
st.markdown("### Ajouter une valeur de capital")
capital_input = st.number_input("Valeur du capital", min_value=0.0, step=100.0)
if st.button("Ajouter"):
    append_capital_value(capital_input)
    st.success("Valeur de capital ajoutée.")
