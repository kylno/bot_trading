import sqlite3
import os

def init_db():
    os.makedirs("data", exist_ok=True)
    conn = sqlite3.connect("data/trades.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            heure TEXT,
            symbole TEXT,
            volume REAL,
            profit REAL,
            strategie TEXT
        )
    """)
    conn.commit()
    conn.close()
    print("✅ Base de données initialisée : trades.db")