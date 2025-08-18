# 🤖 BrainTrader-X1 — Système IA de génération de missions pour colonie fourmilière

Bienvenue dans **BrainTrader-X1**, une ruche IA qui génère des missions autonomes, simule des colonies d’intelligences, exporte des rapports visuels et offre une interface graphique pour piloter tout ça 🐜📊📄

---

## 🧠 Fonctionnalités principales

- 🔁 Génération automatique de missions IA
- 📦 Création de lots de missions pour colonie intelligente
- 🧪 Simulation d’activité de fourmis virtuelles
- 🎨 Générateur de noms IA stylisés (type Shadow-341, Neo-777…)
- 📋 Journalisation CSV automatique des missions
- 📊 Graphiques analytiques avec `matplotlib`
- 📄 Export PDF des rapports d’état avec `fpdf`
- 💌 Envoi de rapports par e-mail (SMTP sécurisé)
- 🖥️ Interface graphique complète en `Tkinter`
- ⚙️ Configuration centralisée via `config.json`
- 🧠 Modules IA spécialisés pour pilotage intelligent
- 🖼️ Interface web Streamlit pilotée par `run_app.py`
- 📂 Navigation dynamique entre agents IA

---

## ⚙️ Arborescence du projet
BrainTrader-X1/ │ ├── run_app.py                 # Lancement cockpit IA ├── menu.py                   # Navigation dynamique (via importlib) ├── agent_cerveaux.py         # Orchestration des IA ├── config.json               # Paramètres système │ ├── dashboard_tk.py           # Interface graphique Tkinter ├── mission_generator.py      # Générateur de missions IA ├── nom_generator.py          # Générateur de noms stylés ├── mailer.py                 # Envoi e-mail SMTP ├── reporter.py               # Générateur PDF │ ├── streamlit_app/ │   ├── dashboard.py │   ├── cockpit_streamlit.py │   ├── centre_de_mission.py │   ├── pages/ │   │   ├── statistiques_ia.py │   │   ├── diagnostic_ia.py │   │   └── pilotage_ia.py │   └── ia_cerveaux/ │       ├── profiteur.py │       ├── accumulateur.py │       ├── casa_de_papel.py │       └── diagnostiqueur.py


---

## 🤖 Agents IA intégrés

Chaque agent IA est encapsulé dans un module et exposé avec une interface uniforme :

| Agent IA         | Fichier              | Classe               | Stratégie par défaut            |
|------------------|----------------------|----------------------|----------------------------------|
| Profiteur        | `profiteur.py`       | `ProfiteurIA`        | trend_following                  |
| Accumulateur     | `accumulateur.py`    | `AccumulateurIA`     | accumulation_passive             |
| Casa De Papel    | `casa_de_papel.py`   | `CasaDePapelIA`      | furtif_arbitrage                 |
| Diagnostiqueur   | `diagnostiqueur.py`  | `DiagnostiqueurIA`   | diagnostic_sante_portefeuille    |

➡️ Chaque IA possède :
- `.analyser(donnees)` → retourne `signal`, `confiance`, `stratégie`
- `.afficher_resume()` → imprime l’état du module IA

---

## 🖥️ Interface cockpit Streamlit

L’interface web permet de piloter tous les modules IA, visualiser les performances, lancer les agents et naviguer entre les vues :

- `dashboard.py` : Vue centrale
- `menu.py` : Navigation dynamique entre modules
- `run_app.py` : Script de démarrage automatique
- `cockpit_streamlit.py` : Vue cockpit étendue

```bash
python run_app.py

# Mon projet Streamlit IA

Projet développé avec Streamlit pour explorer des données et intégrer un modèle IA.

## Installation

```bash
pip install -r requirements.txt