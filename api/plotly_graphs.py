import sqlite3
import plotly.graph_objects as go
import os

DB_PATH = "data/trades.db"
GRAPH_DIR = "static/graphs"

os.makedirs(GRAPH_DIR, exist_ok=True)

def generer_plotly_capital():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT date, SUM(profit) FROM trades GROUP BY date ORDER BY date")
    data = c.fetchall()
    conn.close()

    dates = [d[0] for d in data]
    profits = [d[1] for d in data]
    capital = [sum(profits[:i+1]) for i in range(len(profits))]

    fig = go.Figure(data=go.Scatter(x=dates, y=capital, mode="lines+markers", line=dict(color="#007ACC")))
    fig.update_layout(title="Évolution du capital IA", xaxis_title="Date", yaxis_title="Capital (€)", template="plotly_white")
    fig.write_html(f"{GRAPH_DIR}/capital_interactif.html")

def generer_plotly_strategie():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT strategie, AVG(profit) FROM trades GROUP BY strategie")
    data = c.fetchall()
    conn.close()

    strategies = [d[0] for d in data]
    moyennes = [d[1] for d in data]

    fig = go.Figure(data=go.Bar(x=strategies, y=moyennes, marker_color="#00BFA5"))
    fig.update_layout(title="Profit moyen par stratégie", xaxis_title="Stratégie", yaxis_title="Profit (€)", template="plotly_white")
    fig.write_html(f"{GRAPH_DIR}/strategie_interactive.html")

def generer_plotly_symboles():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT symbole, SUM(profit) FROM trades GROUP BY symbole")
    data = c.fetchall()
    conn.close()

    symboles = [d[0] for d in data]
    profits = [d[1] for d in data]

    fig = go.Figure(data=go.Pie(labels=symboles, values=profits, hole=0.4))
    fig.update_layout(title="Répartition des profits par symbole", template="plotly_white")
    fig.write_html(f"{GRAPH_DIR}/symboles_donut.html")