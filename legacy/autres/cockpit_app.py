import streamlit as st
import pandas as pd
import json
import os

st.set_page_config(page_title="Cockpit IA – Vue Globale", layout="wide")
st.title("🧠 Cockpit IA – Vue Globale des Cerveaux")

DECISIONS_PATH = "decisions.json"
capital_initial = 1000

if os.path.exists(DECISIONS_PATH):
    with open(DECISIONS_PATH, "r") as f:
        decisions = json.load(f)

    df = pd.DataFrame(decisions)
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values("timestamp")

    # Courbe globale
    st.subheader("📈 Capital global (tous cerveaux)")
    capital = capital_initial
    historique = []

    for _, row in df.iterrows():
        gain = capital * (row["variation"] / 100)
        capital += gain
        historique.append({"timestamp": row["timestamp"], "capital": capital})

    df_global = pd.DataFrame(historique)
    st.line_chart(df_global.set_index("timestamp"))
    rendement = ((capital - capital_initial) / capital_initial) * 100
    st.success(f"💰 Capital global simulé : {capital:.2f} (+{rendement:.2f}%)")

    # Fonction pour afficher chaque cerveau
    def afficher_cerveau(df, nom, filtre=None):
        st.subheader(f"🧠 Cerveau : {nom}")
        if filtre:
            df_cerveau = df.query(filtre)
        else:
            df_cerveau = df[df["brain"] == nom]

        if df_cerveau.empty:
            st.info("Aucune donnée pour ce cerveau.")
            return

        capital = capital_initial
        historique = []

        for _, row in df_cerveau.iterrows():
            gain = capital * (row["variation"] / 100)
            capital += gain
            historique.append({"timestamp": row["timestamp"], "capital": capital})

        df_c = pd.DataFrame(historique)
        st.line_chart(df_c.set_index("timestamp"))
        rendement = ((capital - capital_initial) / capital_initial) * 100
        st.success(f"💰 Capital simulé : {capital:.2f} (+{rendement:.2f}%)")
        st.dataframe(df_cerveau[["timestamp", "symbol", "variation", "price"]].sort_values("timestamp", ascending=False))

    # Affichage des cerveaux
    afficher_cerveau(df, "Casa de Papel", "brain == 'casadepapel'")
    afficher_cerveau(df, "Berzerk", "brain == 'berzerk'")
    afficher_cerveau(df, "Microcap Global", "brain.str.contains('microcap')")
    afficher_cerveau(df, "Microcap 1 (50% à 99%)", "brain == 'microcap1'")
    afficher_cerveau(df, "Microcap 2 (100%+)", "brain == 'microcap2'")

else:
    st.warning("Fichier decisions.json introuvable.")
    
    st.title("🧮 Pilotage du Capital")

# Capital de départ
capital_initial = 1000
st.metric("💼 Capital de départ", f"{capital_initial:.2f} €")

# Calcul global
capital_global = capital_initial
for _, row in df.iterrows():
    gain = capital_global * (row["variation"] / 100)
    capital_global += gain
rendement_global = ((capital_global - capital_initial) / capital_initial) * 100
st.metric("📈 Capital actuel", f"{capital_global:.2f} €", f"{rendement_global:.2f}%")

# Détail par cerveau
st.subheader("🧠 Détail par cerveau")
cerveaux = df["brain"].unique()
for cerveau in cerveaux:
    df_c = df[df["brain"] == cerveau]
    capital = capital_initial
    for _, row in df_c.iterrows():
        gain = capital * (row["variation"] / 100)
        capital += gain
    rendement = ((capital - capital_initial) / capital_initial) * 100
    st.metric(f"🧠 {cerveau}", f"{capital:.2f} €", f"{rendement:.2f}%")

# Seuil de perte par cerveau
st.subheader("⚠️ Seuil de perte par cerveau")
seuils = {}
for cerveau in cerveaux:
    seuils[cerveau] = st.slider(f"🔧 Seuil de perte pour {cerveau}", min_value=0, max_value=100, value=30)

# Alerte si perte dépasse seuil
st.subheader("🚨 Surveillance des pertes")
for cerveau in cerveaux:
    df_c = df[df["brain"] == cerveau]
    capital = capital_initial
    for _, row in df_c.iterrows():
        gain = capital * (row["variation"] / 100)
        capital += gain
    perte = capital_initial - capital
    if perte > (capital_initial * seuils[cerveau] / 100):
        st.error(f"⚠️ {cerveau} a dépassé le seuil de perte de {seuils[cerveau]}% !")