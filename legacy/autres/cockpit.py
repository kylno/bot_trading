import streamlit as st
import pandas as pd
import requests
import yfinance as yf
import altair as alt
import datetime
import io
from openpyxl import Workbook
from openpyxl.styles import Font

# 🔗 Modules internes
from bot_trader import detect_signal, executer_ordre
from modules.scanner_ai import ia_decision_engine

# ⚙️ Configuration de la page
st.set_page_config(page_title="Cockpit IA Trading", page_icon="🚀", layout="wide")

# 📋 Barre latérale
st.sidebar.image("images/logo.png", width=150)
st.sidebar.title("📁 Navigation")
menu = st.sidebar.radio("Aller vers :", [
    "Accueil", "Analyse marché", "Pilotage automatique", "Scanner IA", "Historique IA"
])

# 🏠 Accueil
if menu == "Accueil":
    st.title("🚀 Cockpit IA de Trading Mondial")
    st.markdown("Bienvenue Kylian. Ce cockpit te permet d’analyser, surveiller et piloter automatiquement tous les marchés mondiaux.")
    st.markdown("Tape un symbole pour commencer (ex: `BTCUSDT`, `AAPL`, `CAC40`, `EURUSD`, `GOLD`).")

# 🔍 Analyse marché
elif menu == "Analyse marché":
    st.title("📊 Analyse du marché")
    symbole = st.text_input("🔍 Rechercher un actif mondial", value="BTCUSDT")

    def detecter_domaine(symbole):
        symbole = symbole.upper()
        if symbole.endswith("USDT") or symbole in ["BTC", "ETH", "SOL"]:
            return "crypto"
        elif symbole in ["EURUSD", "GBPJPY", "USDJPY"]:
            return "forex"
        elif symbole in ["GOLD", "OIL", "WTI"]:
            return "commodity"
        elif symbole in ["CAC40", "DAX", "SP500"]:
            return "indice"
        else:
            return "action"

    def calcul_rsi(data, period=14):
        delta = data.diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=period).mean()
        avg_loss = loss.rolling(window=period).mean()
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        return rsi

    def calcul_sma(data, period=20):
        return data.rolling(window=period).mean()

    def calcul_ema(data, period=20):
        return data.ewm(span=period, adjust=False).mean()

    if symbole:
        domaine = detecter_domaine(symbole)
        type_graphique = st.selectbox("📊 Type de graphique", ["Ligne", "Zone", "Barre"])
        indicateurs = st.multiselect("📐 Indicateurs techniques", ["RSI", "SMA", "EMA"])

        if domaine == "crypto":
            url = "https://api.binance.com/api/v3/klines"
            params = {"symbol": symbole.upper(), "interval": "1d", "limit": 100}
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

                st.subheader(f"📈 {symbole.upper()} - Crypto (Binance)")

                if "RSI" in indicateurs:
                    df["RSI"] = calcul_rsi(df["Close"])
                    st.line_chart(df.set_index("Open time")["RSI"], height=150)
                if "SMA" in indicateurs:
                    df["SMA"] = calcul_sma(df["Close"])
                if "EMA" in indicateurs:
                    df["EMA"] = calcul_ema(df["Close"])

                base = alt.Chart(df).encode(x='Open time')
                courbe = base.mark_line(color="orange").encode(y='Close') if type_graphique == "Ligne" else \
                         base.mark_area(color="lightblue", opacity=0.6).encode(y='Close') if type_graphique == "Zone" else \
                         base.mark_bar(color="teal").encode(y='Close')

                overlays = []
                if "SMA" in indicateurs:
                    overlays.append(base.mark_line(color="blue").encode(y='SMA'))
                if "EMA" in indicateurs:
                    overlays.append(base.mark_line(color="purple").encode(y='EMA'))

                chart = courbe
                for overlay in overlays:
                    chart += overlay

                st.altair_chart(chart.properties(title=f"{symbole.upper()} - Prix de clôture"), use_container_width=True)
                st.metric("Dernier prix", f"{df['Close'].iloc[-1]:.2f} USDT")
            else:
                st.error("❌ Symbole crypto invalide ou API Binance inaccessible.")

        else:
            try:
                actif = yf.Ticker(symbole)
                hist = actif.history(period="3mo")
                if not hist.empty:
                    st.subheader(f"📈 {symbole.upper()} - {domaine.capitalize()} (Yahoo Finance)")
                    hist["Close"] = hist["Close"].astype(float)
                    if "RSI" in indicateurs:
                        hist["RSI"] = calcul_rsi(hist["Close"])
                        st.line_chart(hist["RSI"], height=150)
                    if "SMA" in indicateurs:
                        hist["SMA"] = calcul_sma(hist["Close"])
                    if "EMA" in indicateurs:
                        hist["EMA"] = calcul_ema(hist["Close"])

                    base = alt.Chart(hist.reset_index()).encode(x='Date')
                    courbe = base.mark_line(color="green").encode(y='Close') if type_graphique == "Ligne" else \
                             base.mark_area(color="lightgreen", opacity=0.6).encode(y='Close') if type_graphique == "Zone" else \
                             base.mark_bar(color="darkgreen").encode(y='Close')

                    overlays = []
                    if "SMA" in indicateurs:
                        overlays.append(base.mark_line(color="blue").encode(y='SMA'))
                    if "EMA" in indicateurs:
                        overlays.append(base.mark_line(color="purple").encode(y='EMA'))

                    chart = courbe
                    for overlay in overlays:
                        chart += overlay

                    st.altair_chart(chart.properties(title=f"{symbole.upper()} - Prix de clôture"), use_container_width=True)
                    st.metric("Dernier prix", f"{hist['Close'].iloc[-1]:.2f}")
                else:
                    st.warning("⚠️ Aucun historique trouvé pour ce symbole.")
            except Exception as e:
                st.error(f"Erreur lors de la récupération : {e}")

# 🤖 Pilotage automatique
elif menu == "Pilotage automatique":
    st.title("🤖 Pilotage automatique du bot")
    symbole_bot = st.text_input("🔍 Actif à surveiller (ex: BTCUSDT)")
    seuil = st.number_input("🎯 Seuil d'achat", value=30000.0)
    montant = st.number_input("💰 Montant à investir (USDT)", value=100.0)

    if st.button("🚀 Activer le bot"):
        signal = detect_signal(symbole_bot.upper(), seuil_achat=seuil)
        if signal == "achat":
            executer_ordre(symbole_bot.upper(), montant)
            st.success("✅ Ordre d'achat exécuté automatiquement")
        elif signal == "attente":
            st.info("⏳ Pas de signal d'achat pour le moment")
        else:
            st.error("❌ Erreur lors de la détection du signal.")

# 🧠 Scanner IA
elif menu == "Scanner IA":
    st.title("🧠 Scanner IA stratégique")
    if st.button("🔍 Lancer une décision IA"):
        message = ia_decision_engine()
        st.success(message)

# 📜 Historique IA
elif menu == "Historique IA":
    st.title("📜 Historique complet des décisions IA")

    def parser_logs_en_dataframe(fichier):
        try:
            with open(fichier, "r") as f:
                lignes = f.readlines()
            data = []
            for ligne in lignes:
                if " - " in ligne:
                    ts, msg = ligne.strip().split(" - ", 1)
                    try:
                        date = datetime.datetime.strptime(ts, "%a %b %d %H:%M:%S %Y")
                    except:
                        date = ts
                    data.append({"Horodatage": date, "Message": msg})
            return pd.DataFrame(data)
        except:
            return pd.DataFrame()

    def exporter_excel(df):
        wb = Workbook()
        ws = wb.active
        ws.title = "Historique IA"
        headers = list(df.columns)
        ws.append(headers)
        for cell in ws[1]:
            cell.font = Font(bold=True)
        for _, row in df.iterrows():
            ws.append(list(row))
        buffer = io.BytesIO()
        wb.save(buffer)
        buffer.seek