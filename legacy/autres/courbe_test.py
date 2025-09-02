import streamlit as st
import pandas as pd
import requests
import altair as alt

st.set_page_config(page_title="Test Courbe Binance", page_icon="📈", layout="wide")
st.title("📈 Test d'affichage de la courbe Binance")

# 🔍 Entrée du symbole
symbole = st.text_input("Tapez un symbole Binance (ex: BTCUSDT, ETHUSDT)", value="BTCUSDT")

if symbole:
    url = "https://api.binance.com/api/v3/klines"
    params = {
        "symbol": symbole.upper(),
        "interval": "1d",
        "limit": 100
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        raw_data = response.json()
        df = pd.DataFrame(raw_data, columns=[
            "Open time", "Open", "High", "Low", "Close", "Volume",
            "Close time", "Quote asset volume", "Number of trades",
            "Taker buy base volume", "Taker buy quote volume", "Ignore"
        ])
        df["Open time"] = pd.to_datetime(df["Open time"], unit='ms')
        df["Close"] = df["Close"].astype(float)

        st.subheader(f"📉 Courbe de clôture pour {symbole.upper()}")
        chart = alt.Chart(df).mark_line(color="blue").encode(
            x='Open time',
            y='Close'
        ).properties(title=f"{symbole.upper()} - Prix de clôture (100 derniers jours)")

        st.altair_chart(chart, use_container_width=True)
    else:
        st.error("❌ Symbole invalide ou API Binance inaccessible.")