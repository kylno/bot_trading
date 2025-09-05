import streamlit as st
import pyttsx3
import os
import sys
import random

# 📍 Chemin local pour VS Code
sys.path.append(os.path.dirname(__file__))

# 📦 Import des cerveaux IA
from ia_cerveaux import (
    ProfiteurIA,
    AccumulateurIA,
    CasaDePapelIA,
    DiagnostiqueurIA,
    StrategisteFantome
)

# 🧠 Instanciation des IA
agents = {
    "profiteur": ProfiteurIA(),
    "accumulateur": AccumulateurIA(),
    "casa": CasaDePapelIA(),
    "diagnostiqueur": DiagnostiqueurIA(),
    "fantome": StrategisteFantome()
}

# 🔊 Synthèse vocale
@st.cache_resource
def init_moteur():
    return pyttsx3.init()

def parler(message, vitesse=150, volume=1.0, voix_index=0):
    moteur = init_moteur()
    moteur.setProperty("rate", vitesse)
    moteur.setProperty("volume", volume)
    voices = moteur.getProperty("voices")
    if voix_index < len(voices):
        moteur.setProperty("voice", voices[voix_index].id)
    moteur.say(message)
    moteur.runAndWait()

# 🔖 Cartes de personnalité IA
def afficher_fantome():
    st.markdown("## 🕶️ Carte d’identité : Le Stratégiste Fantôme")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Ninja_shadow_silhouette.svg/800px-Ninja_shadow_silhouette.svg.png", width=150)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Style** : Discret, méthodique, imprévisible")
        st.write("**Spécialité** : Manœuvres invisibles")
    with col2:
        st.write("**Couleur** : 🖤 Noire comme l’ombre")
        st.write("**Esprit** : Silencieux mais percutant")
    st.divider()
    st.success(f"🧠 *« {agents['fantome'].conseiller()} »*")

def afficher_profiteur():
    st.markdown("## 💼 Carte d’identité : Le Profiteur")
    st.image("https://cdn-icons-png.flaticon.com/512/2756/2756951.png", width=150)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Style** : Opportuniste, réactif, rusé")
        st.write("**Spécialité** : Profit immédiat")
    with col2:
        st.write("**Couleur** : 🟠 Orange audacieux")
        st.write("**Réputation** : Rapide… et risqué")
    st.divider()
    st.success("🧠 *« Ce qui tombe, je prends. Ce qui brille, j'agis. »*")

def afficher_accumulateur():
    st.markdown("## 💰 Carte d’identité : L’Accumulateur")
    st.image("https://cdn-icons-png.flaticon.com/512/2913/2913990.png", width=150)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Style** : Patient, méthodique")
        st.write("**Spécialité** : Ressources long terme")
    with col2:
        st.write("**Couleur** : 🟢 Vert sécurisé")
        st.write("**Réputation** : Préparé à tout")
    st.divider()
    st.success("🧠 *« Celui qui accumule devient maître du futur. »*")

def afficher_diagnostiqueur():
    st.markdown("## 🔍 Carte d’identité : Le Diagnostiqueur")
    st.image("https://cdn-icons-png.flaticon.com/512/2889/2889671.png", width=150)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Style** : Observateur, critique")
        st.write("**Spécialité** : Détection des failles")
    with col2:
        st.write("**Couleur** : 🔵 Bleu analytique")
        st.write("**Réputation** : Rien ne lui échappe")
    st.divider()
    st.success("🧠 *« Tout problème a un noyau. Je le perce. »*")

def afficher_casa():
    st.markdown("## 🎭 Carte d’identité : Casa De Papel")
    st.image("https://upload.wikimedia.org/wikipedia/commons/a/a7/Anonymous_emblem.svg", width=150)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Style** : Cérébral, manipulateur")
        st.write("**Spécialité** : Plans complexes")
    with col2:
        st.write("**Couleur** : 🔴 Rouge révolutionnaire")
        st.write("**Réputation** : Subtil mais spectaculaire")
    st.divider()
    st.success("🧠 *« La meilleure attaque est celle qu’on ne comprend qu’après. »*")

# ⚔️ Duel entre deux IA
def duel_ia(agent1, agent2):
    st.markdown(f"## ⚔️ Duel entre `{agent1.nom}` et `{agent2.nom}`")
    col1, col2 = st.columns(2)
    score1 = random.randint(1, 100)
    score2 = random.randint(1, 100)
    with col1:
        st.markdown(f"### 🧠 {agent1.nom}")
        st.info(agent1.conseiller())
        st.progress(score1 / 100)
        st.write(f"**Impact stratégique** : {score1}/100")
    with col2:
        st.markdown(f"### 🧠 {agent2.nom}")
        st.info(agent2.conseiller())
        st.progress(score2 / 100)
        st.write(f"**Impact stratégique** : {score2}/100")
    st.divider()
    if score1 > score2:
        st.success(f"🏆 **{agent1.nom}** remporte le duel !")
    elif score2 > score1:
        st.success(f"🏆 **{agent2.nom}** l’emporte avec brio !")
    else:
        st.warning("⚖️ Égalité parfaite !")

# 🖥️ Interface Streamlit
st.set_page_config(page_title="Cockpit IA", layout="wide")
st.title("🧠 Cockpit des Cerveaux IA")

# 🎴 Sélection et affichage de carte
choix = st.selectbox("👨‍💻 Sélectionne une IA :", list(agents.keys()))
if choix == "profiteur":
    afficher_profiteur()
elif choix == "accumulateur":
    afficher_accumulateur()
elif choix == "diagnostiqueur":
    afficher_diagnostiqueur()
elif choix == "casa":
    afficher_casa()
elif choix == "fantome":
    afficher_fantome()

# 🔊 Synthèse vocale
if st.button("🔊 Faire parler l'IA"):
    parler(agents[choix].conseiller())

# 🎮 Zone de duel IA
st.markdown("---")
st.header("🥋 Duel stratégique entre cerveaux IA")
ia1 = st.selectbox("🤖 Choisis le premier cerveau :", list(agents.keys()), key="duel1")
ia2 = st.selectbox("🤖 Choisis le second cerveau :", list(agents.keys()), key="duel2")
if ia1 != ia2:
    if st.button("🚀 Lancer le duel !"):
        duel_ia(agents[ia1], agents[ia2])
else:
    st.info("🙃 Sélectionne deux IA différentes pour comparer leurs stratégies.")
    
    agents = {
    "profiteur": ProfiteurIA(),
    "accumulateur": AccumulateurIA(),
    "casa": CasaDePapelIA(),
    "diagnostiqueur": DiagnostiqueurIA(),
    "fantome": StrategisteFantome(),
    "berzerk": BerzerkIA(),
    "microcap1": microcap1(),
    "microcap2": microcap2()
}
    
    def afficher_berzerk():
     st.markdown("## ⚡ Carte d’identité : Berzerk+")
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=150)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Style** : Agressif, rapide, répétitif")
        st.write("**Spécialité** : Scalping intensif")
    with col2:
        st.write("**Couleur** : 🔥 Rouge vif")
        st.write("**Réputation** : Frappe courte, frappe souvent")
    st.divider()
    st.success(f"🧠 *« {agents['berzerk'].conseiller()} »*") 
    
    def afficher_microcap1():
     st.markdown("## 📈 Carte d’identité : Microcap 1")
    st.image("https://cdn-icons-png.flaticon.com/512/2910/2910791.png", width=150)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Style** : Explorateur, visionnaire")
        st.write("**Spécialité** : Détection de pépites")
    with col2:
        st.write("**Couleur** : 🟡 Jaune spéculatif")
        st.write("**Réputation** : Parie sur l’inattendu")
    st.divider()
    st.success(f"🧠 *« {agents['microcap1'].conseiller()} »*")
    
    def afficher_microcap2():
     st.markdown("## 📉 Carte d’identité : Microcap 2")
    st.image("https://cdn-icons-png.flaticon.com/512/2910/2910795.png", width=150)
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Style** : Sniper, discret, tactique")
        st.write("**Spécialité** : Exploitation de faibles volumes")
    with col2:
        st.write("**Couleur** : 🧊 Bleu glacial")
        st.write("**Réputation** : Fait exploser ce que personne ne regarde")
    st.divider()
    st.success(f"🧠 *« {agents['microcap2'].conseiller()} »*")
