import requests, json
from datetime import datetime

def get_all_crypto_market_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "eur",
        "order": "market_cap_desc",
        "per_page": 250,
        "page": 1,
        "price_change_percentage": "1h,24h,7d"
    }
    all_data = []
    for page in range(1, 10):  # Jusqu'à 2500 cryptos
        params["page"] = page
        response = requests.get(url, params=params)
        if response.status_code != 200:
            break
        all_data += response.json()
    return all_data

def scanner_cryptos():
    cryptos = get_all_crypto_market_data()
    opportunities = []

    for coin in cryptos:
        try:
            name = coin['name']
            symbol = coin['symbol']
            price = coin['current_price']
            vol = coin['total_volume']
            change_1h = coin['price_change_percentage_1h_in_currency']
            change_24h = coin['price_change_percentage_24h_in_currency']
            change_7d = coin['price_change_percentage_7d_in_currency']

            score = 0
            if change_1h > 3: score += 2
            if change_24h > 8: score += 3
            if change_7d > 20: score += 4
            if vol > 5_000_000: score += 2

            if score >= 7:
                opportunities.append({
                    "timestamp": datetime.now().isoformat(),
                    "nom": name,
                    "symbol": symbol.upper(),
                    "score": score,
                    "prix": price,
                    "volume": vol,
                    "change_1h": change_1h,
                    "change_24h": change_24h,
                    "change_7d": change_7d
                })
        except:
            continue

    with open("logs/opportunites_crypto.json", "w", encoding="utf-8") as f:
        json.dump(opportunities, f, indent=2)

    return opportunities