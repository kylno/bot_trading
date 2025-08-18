import sqlite3
import matplotlib.pyplot as plt
import os
from datetime import datetime

DB_PATH = "data/trades.db"

# 🔍 Filtrer les trades selon critères
def filtrer_trades(filtres):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    query = "SELECT * FROM trades WHERE 1=1"
    params = []

    if filtres.get("symbole"):
        query += " AND symbole = ?"
        params.append(filtres["symbole"])
    if filtres.get("strategie"):
        query += " AND strategie = ?"
        params.append(filtres["strategie"])
    if filtres.get("date_debut"):
        query += " AND date >= ?"
        params.append(filtres["date_debut"])
    if filtres.get("date_fin"):
        query += " AND date <= ?"
        params.append(filtres["date_fin"])

    query += " ORDER BY date, heure"
    c.execute(query, params)
    trades = [ dict(zip(["id", "date", "heure", "symbole", "volume", "profit", "strategie"], row)) for row in c.fetchall() ]
    conn.close()
    return trades

# 📈 Générer l’évolution du capital
def generer_graphe_performance():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT date, SUM(profit) FROM trades GROUP BY date ORDER BY date")
    donnees = c.fetchall()
    conn.close()

    dates = [ d[0] for d in donnees ]
    profits = [ d[1] for d in donnees ]
    capital = [ sum(profits[:i+1]) for i in range(len(profits)) ]

    plt.figure(figsize=(10,4))
    plt.plot(dates, capital, color="#007ACC", marker="o")
    plt.title("Évolution du capital IA")
    plt.xlabel("Date")
    plt.ylabel("Capital cumulatif (€)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("static/capital_graph.png")
    plt.close()

# 📊 Générer profit moyen par stratégie
def generer_graphe_par_strategie():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT strategie, AVG(profit) FROM trades GROUP BY strategie")
    donnees = c.fetchall()
    conn.close()

    strategies = [ d[0] for d in donnees ]
    moyennes = [ d[1] for d in donnees ]

    plt.figure(figsize=(8,4))
    plt.bar(strategies, moyennes, color="#00BFA5")
    plt.title("Profit moyen par stratégie")
    plt.xlabel("Stratégie")
    plt.ylabel("Profit moyen (€)")
    plt.tight_layout()
    plt.savefig("static/strategie_graph.png")
    plt.close()

# 🧮 Jauge IA
def calculer_jauge_performance_sql():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM trades")
    total = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM trades WHERE profit > 0")
    gagnants = c.fetchone()[0]
    conn.close()

    taux = 100 * gagnants / total if total else 0
    return f"{round(taux, 1)}%"

# ➕ Ajouter un trade
def ajouter_trade_sql(data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO trades (date, heure, symbole, volume, profit, strategie)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (data["date"], data["heure"], data["symbole"], float(data["volume"]),
          float(data["profit"]), data["strategie"]))
    conn.commit()
    conn.close()

# 🖊️ Modifier un trade
def modifier_trade(id, data):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("""
        UPDATE trades SET date=?, heure=?, symbole=?, volume=?, profit=?, strategie=?
        WHERE id=?
    """, (data["date"], data["heure"], data["symbole"], float(data["volume"]),
          float(data["profit"]), data["strategie"], id))
    conn.commit()
    conn.close()

# 🗑️ Supprimer un trade
def supprimer_trade(id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("DELETE FROM trades WHERE id=?", (id,))
    conn.commit()
    conn.close()

# 🔎 Récupérer un trade spécifique
def get_trade(id):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM trades WHERE id=?", (id,))
    row = c.fetchone()
    conn.close()
    if row:
        return dict(zip(["id", "date", "heure", "symbole", "volume", "profit", "strategie"], row))
    return None

# 📊 Récupérer les statistiques
def get_stats():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("SELECT symbole, SUM(profit) FROM trades GROUP BY symbole")
    symboles = [ { "symbole": s[0], "profit_total": round(s[1], 2) } for s in c.fetchall() ]

    c.execute("SELECT strategie, AVG(profit) FROM trades GROUP BY strategie")
    strategies = [ { "strategie": s[0], "profit_moyen": round(s[1], 2) } for s in c.fetchall() ]

    c.execute("SELECT COUNT(*) FROM trades")
    total = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM trades WHERE profit > 0")
    gagnants = c.fetchone()[0]
    c.execute("SELECT COUNT(*) FROM trades WHERE profit <= 0")
    perdants = c.fetchone()[0]
    conn.close()

    return {
        "symboles": symboles,
        "strategies": strategies,
        "totaux": {
            "total_trades": total,
            "gagnants": gagnants,
            "perdants": perdants
        }
    }

# 🕒 Dernier trade
def get_last_trade():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM trades ORDER BY date DESC, heure DESC LIMIT 1")
    row = c.fetchone()
    conn.close()
    if row:
        return dict(zip(["id", "date", "heure", "symbole", "volume", "profit", "strategie"], row))
    return {}
