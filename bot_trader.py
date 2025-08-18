import json
import random
import csv
from datetime import datetime
import yfinance as yf
import plotly.graph_objects as go

# 📁 Chemins
config_path = "logs/config_ia.json"
log_path = "logs/ia_log.txt"

# 📦 Charger la config
def charger_config():
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "montant_par_trade": 100,
            "securisation_gain": 0.1
        }

# 💾 Sauvegarder dans le journal IA
def log_ia(message):
    now = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"{now} - {message}\n")

# 📈 Récupérer le prix réel du marché
def get_prix_reel(symbole):
    try:
        data = yf.Ticker(symbole)
        prix = data.history(period="1d")["Close"].iloc[-1]
        return prix
    except Exception as e:
        log_ia(f"⚠️ Erreur récupération prix réel pour {symbole} : {e}")
        return None

# 🔍 Détection de signal avec prix réel
def detect_signal(symbole, seuil_achat):
    prix_actuel = get_prix_reel(symbole)
    if prix_actuel is None:
        log_ia(f"❌ Impossible de récupérer le prix pour {symbole}")
        return "erreur"

    if prix_actuel <= seuil_achat:
        log_ia(f"✅ Signal détecté : IA investit sur {symbole} à {prix_actuel:.2f}")
        return "achat"
    else:
        log_ia(f"⏳ Aucun signal sur {symbole} (prix = {prix_actuel:.2f})")
        return "attente"

# 🧠 Exécution d’un ordre avec sécurisation
def executer_ordre(symbole, capital_total=None):
    config = charger_config()
    montant_trade = config.get("montant_par_trade", 100)
    taux_securisation = config.get("securisation_gain", 0.1)

    prix_achat = get_prix_reel(symbole)
    if prix_achat is None:
        log_ia(f"❌ Trade annulé : prix indisponible pour {symbole}")
        return capital_total if capital_total is not None else 0, 0

    # 💸 Simulation de vente avec gain aléatoire
    prix_vente = prix_achat * random.uniform(1.01, 1.3)

    gain = prix_vente - prix_achat
    montant_gagné = (gain / prix_achat) * montant_trade
    montant_securisé = montant_gagné * taux_securisation
    montant_libre = montant_gagné - montant_securisé

    # 🧾 Journalisation
    log_ia(f"💰 Achat {symbole} à {prix_achat:.2f}, vente simulée à {prix_vente:.2f}")
    log_ia(f"📈 Gain brut : {montant_gagné:.2f} €")
    log_ia(f"🔒 Sécurisé : {montant_securisé:.2f} €, Réinvestissable : {montant_libre:.2f} €")

    # 🧠 Mise à jour du capital
    if capital_total is not None:
        capital_total += montant_libre
        return capital_total, montant_securisé
    else:
        return montant_gagné, montant_securisé

# 📁 Sauvegarder le récapitulatif dans un fichier CSV
def sauvegarder_recap_csv(recap, fichier="logs/recap_trades.csv"):
    try:
        with open(fichier, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["symbole", "capital_après", "gain_sécurisé"])
            writer.writeheader()
            for ligne in recap:
                writer.writerow(ligne)
        log_ia(f"📁 Récapitulatif sauvegardé dans {fichier}")
    except Exception as e:
        log_ia(f"⚠️ Erreur sauvegarde CSV : {e}")

# 📊 Générer un graphique interactif des gains
def afficher_graphique_interactif(recap):
    symboles = [ligne["symbole"] for ligne in recap]
    gains = [ligne["gain_sécurisé"] for ligne in recap]

    fig = go.Figure(data=[
        go.Bar(x=symboles, y=gains, marker_color='mediumseagreen')
    ])
    fig.update_layout(
        title="🔐 Gains sécurisés par symbole",
        xaxis_title="Symbole",
        yaxis_title="Gain sécurisé (€)",
        template="plotly_white"
    )

    horodatage = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_fichier = f"logs/gains_securises_{horodatage}.html"
    fig.write_html(nom_fichier)
    log_ia(f"📊 Graphique interactif sauvegardé : {nom_fichier}")
    print(f"✅ Graphique interactif enregistré : {nom_fichier}")

# 🚀 Simulation multi-symboles
if __name__ == "__main__":
    symboles = {
        "AAPL": 150,
        "TSLA": 250,
        "NVDA": 400,
        "BTC-USD": 30000,
        "ETH-USD": 2000
    }

    capital_initial = 1000
    capital_total = capital_initial
    recap = []

    print("🚀 Simulation multi-symboles en cours...\n")

    for symbole, seuil in symboles.items():
        decision = detect_signal(symbole, seuil)
        if decision == "achat":
            capital_total, securisé = executer_ordre(symbole, capital_total)
            recap.append({
                "symbole": symbole,
                "capital_après": round(capital_total, 2),
                "gain_sécurisé": round(securisé, 2)
            })
        elif decision == "attente":
            print(f"⏳ {symbole} : Pas de signal d’achat")
        else:
            print(f"❌ {symbole} : Erreur récupération prix")

    # 📋 Affichage du tableau récapitulatif
    print("\n📊 Récapitulatif des trades simulés :")
    print(f"{'Symbole':<10} {'Capital (€)':<15} {'Sécurisé (€)':<15}")
    print("-" * 40)
    for ligne in recap:
        print(f"{ligne['symbole']:<10} {ligne['capital_après']:<15} {ligne['gain_sécurisé']:<15}")

    print(f"\n💼 Capital initial : {capital_initial:.2f} €")
    print(f"💰 Capital final   : {capital_total:.2f} €")

    # 📁 Sauvegarde CSV + graphique
    sauvegarder_recap_csv(recap)
    afficher_graphique_interactif(recap)