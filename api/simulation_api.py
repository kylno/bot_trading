# api/simulation.py

def get_bot_config():
    return {
        "strategy": "scalping",
        "risk_level": "medium",
        "max_drawdown": 0.15
    }

def get_performance():
    return {
        "profit": 1250.75,
        "trades": 48,
        "win_rate": 0.67
    }

def get_alerts():
    return [
        {"symbol": "BTC", "score": 92, "type": "buy"},
        {"symbol": "ETH", "score": 78, "type": "sell"}
    ]