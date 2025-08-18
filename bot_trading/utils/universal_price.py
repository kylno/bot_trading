# universal_price.py

import requests
import yfinance as yf

BINANCE_ENDPOINT = "https://api.binance.com/api/v3/ticker/price"

def get_binance_price(symbol):
    symbol_pair = f"{symbol.upper()}USDT"
    try:
        response = requests.get(BINANCE_ENDPOINT, params={"symbol": symbol_pair}, timeout=5)
        data = response.json()
        return float(data["price"])
    except:
        return None

def get_yahoo_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        price = ticker.info.get("regularMarketPrice")
        return price
    except:
        return None

def get_price(symbol):
    """
    Interroge Binance si symbol est crypto,
    sinon interroge Yahoo Finance (action/ETF/index)
    """
    price = get_binance_price(symbol)
    if price is not None:
        return f"🪙 Crypto {symbol.upper()} ➤ {price:.4f} USDT"

    price = get_yahoo_price(symbol)
    if price is not None:
        return f"📈 Actif boursier {symbol.upper()} ➤ {price:.2f} USD"

    return f"❌ Symbole '{symbol}' non reconnu sur Binance ou Yahoo Finance."