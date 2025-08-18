import requests

def get_crypto_price(symbol="bitcoin", currency="eur"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies={currency}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()[symbol][currency]
    return None