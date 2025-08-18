import asyncio
from datetime import datetime
from binance import AsyncClient, BinanceSocketManager

THRESHOLD_PERCENT = 0.0001  # Seuil hyper sensible pour tester facilement
SYMBOL = "btcusdt"          # Token surveillé (en minuscules)

last_price = None

def variation(p1, p2):
    if not p1 or p1 == 0:
        return 0
    return ((p2 - p1) / p1) * 100

async def watch_price():
    global last_price
    client = await AsyncClient.create()
    bsm = BinanceSocketManager(client)
    socket = bsm.symbol_ticker_socket(SYMBOL)

    print(f"🎧 [Berserk Live] Surveillance temps réel de {SYMBOL.upper()}...")

    async with socket as stream:
        while True:
            res = await stream.recv()
            # DEBUG : voir le message brut
            # print("📨 Reçu :", res)

            try:
                new_price = float(res['c'])  # 'c' = prix actuel
            except (KeyError, ValueError) as e:
                print(f"❌ Erreur lecture prix : {e}")
                continue

            now = datetime.now().strftime("%H:%M:%S.%f")[:-3]

            if last_price:
                delta = variation(last_price, new_price)
                print(f"⚙️ Δ = {round(delta, 6)}%")  # ← Ajout pour voir les micro-mouvements

                if abs(delta) >= THRESHOLD_PERCENT:
                    print(f"🚨 [{now}] Variation détectée : {round(delta, 6)}% → {new_price} USD")

                    with open("logs/trades.log", "a", encoding="utf-8") as log:
                        log.write(f"{datetime.now()} [BerserkLive] Δ {round(delta, 6)}% → {new_price} USD\n")

            last_price = new_price

    await client.close_connection()

asyncio.run(watch_price())