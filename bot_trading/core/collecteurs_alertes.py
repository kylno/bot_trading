import time
import json
from datetime import datetime
import os

# 📦 Simulations de sources (à remplacer par des API réelles)
def capter_twitter():
    return [
        {"source": "X", "texte": "Bitcoin pump imminent", "timestamp": datetime.now().isoformat()},
        {"source": "X", "texte": "Apple annonce un nouveau split", "timestamp": datetime.now().isoformat()}
    ]

def capter_discord():
    return [
        {"source": "Discord", "texte": "Solana breakout 12%", "timestamp": datetime.now().isoformat()}
    ]

def capter_google_news():
    return [
        {"source": "News", "texte": "ETF Ethereum validé par SEC", "timestamp": datetime.now().isoformat()}
    ]

# 🧠 Moteur de collecte
def collecter_alertes():
    return [
        {"source": "X", "texte": "Bitcoin pump imminent", "timestamp": "2025-07-17T12:00:00"},
        {"source": "News", "texte": "Apple chute brutale", "timestamp": "2025-07-17T12:01:00"}
    ]