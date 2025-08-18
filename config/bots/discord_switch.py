import discord
from discord.ext import commands
import json
import os
from utils.universal_price import get_price  # Module universel multi-marchés

# 🔐 Ton token Discord
TOKEN = "TON_TOKEN_ICI"

CONFIG_PATH = "config_mode.json"
CAPITAL_PATH = "capital.json"
LOG_PATH = "fourmi_log.csv"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# 🔁 Changement de mode IA
def changer_mode(auto: bool):
    with open(CONFIG_PATH, "w") as f:
        json.dump({"auto_mode": auto}, f, indent=2)

def lire_mode():
    try:
        with open(CONFIG_PATH, "r") as f:
            return json.load(f).get("auto_mode", False)
    except:
        return False

# 🎛️ !mode
@bot.command()
async def mode(ctx, arg):
    arg = arg.lower()
    if arg == "auto":
        changer_mode(True)
        await ctx.send("✅ Mode AUTO activé. L’IA agit en autonomie 🤖")
    elif arg == "manuel":
        changer_mode(False)
        await ctx.send("🛑 Mode MANUEL activé. Surveillance uniquement 🧠")
    else:
        await ctx.send("❓ Utilise `!mode auto` ou `!mode manuel`")

# 📡 !status
@bot.command()
async def status(ctx):
    mode = "AUTO 🤖" if lire_mode() else "MANUEL 🧠"
    await ctx.send(f"📡 Mode IA actuel : **{mode}**")

# 💰 !capital
@bot.command()
async def capital(ctx):
    try:
        with open(CAPITAL_PATH, "r") as f:
            capital = json.load(f).get("capital", {})
        if not capital:
            await ctx.send("📁 Portefeuille vide ou corrompu.")
            return
        msg = "💰 **Portefeuille simulé** :\n" + "\n".join([f"• {k}: {v:.4f}" for k, v in capital.items()])
        await ctx.send(msg)
    except:
        await ctx.send("❌ Erreur lors de la lecture de capital.json.")

# 🔄 !reset
@bot.command()
async def reset(ctx, amount: float = 1000):
    try:
        with open(CAPITAL_PATH, "r") as f:
            capital = json.load(f).get("capital", {})
        capital["USDT"] = amount
        for k in capital:
            if k != "USDT":
                capital[k] = 0.0
        with open(CAPITAL_PATH, "w") as f:
            json.dump({"capital": capital}, f, indent=2)
        await ctx.send(f"🔁 Capital IA réinitialisé à {amount:.2f} USDT.")
    except:
        await ctx.send("❌ Erreur pendant le reset.")

# 🛒 !buy
@bot.command()
async def buy(ctx, symbol: str, amount: float):
    symbol = symbol.upper()
    try:
        with open(CAPITAL_PATH, "r+") as f:
            data = json.load(f)
            capital = data.get("capital", {})
            usdt = capital.get("USDT", 0)

            if amount > usdt:
                await ctx.send(f"🚫 Fonds insuffisants : USDT = {usdt:.2f}")
                return

            capital["USDT"] -= amount
            capital[symbol] = capital.get(symbol, 0) + 1  # quantité fictive
            f.seek(0)
            json.dump({"capital": capital}, f, indent=2)
            f.truncate()

        with open(LOG_PATH, "a") as log:
            log.write(f"BUY MANUAL {symbol} {amount:.2f} USDT\n")

        await ctx.send(f"✅ Achat manuel : {amount:.2f} USDT → {symbol}")
    except:
        await ctx.send("❌ Erreur pendant l’achat manuel.")

# 💥 !sell_all
@bot.command()
async def sell_all(ctx):
    try:
        with open(CAPITAL_PATH, "r+") as f:
            capital = json.load(f).get("capital", {})
            capital["USDT"] += 100  # gain fictif
            f.seek(0)
            json.dump({"capital": capital}, f, indent=2)
            f.truncate()

        with open(LOG_PATH, "a") as log:
            log.write("SELL_ALL command triggered (manuel)\n")

        await ctx.send("💥 Positions IA simulées liquidées. Gain fictif ajouté.")
    except:
        await ctx.send("❌ Erreur durant la vente forcée.")

# 📋 !stats
@bot.command()
async def stats(ctx):
    try:
        if not os.path.exists(LOG_PATH):
            await ctx.send("📄 Aucun log trouvé.")
            return
        with open(LOG_PATH, "r") as f:
            lines = f.readlines()[-3:]
        if not lines:
            await ctx.send("📄 Aucun trade enregistré.")
            return
        msg = "📋 **Derniers trades IA** :\n" + "".join(f"• `{line.strip()}`\n" for line in lines)
        await ctx.send(msg)
    except:
        await ctx.send("❌ Erreur de lecture du journal.")

# 🚨 !force_alert
@bot.command()
async def force_alert(ctx):
    await ctx.send("🚨 Alerte IA simulée ! Ceci est un test.")

# 💲 !price
@bot.command()
async def price(ctx, symbol: str):
    msg = get_price(symbol)
    await ctx.send(msg)

# 💼 !wallet
@bot.command()
async def wallet(ctx):
    try:
        with open(CAPITAL_PATH, "r") as f:
            capital = json.load(f).get("capital", {})
    except:
        await ctx.send("❌ Erreur de lecture du portefeuille.")
        return

    msg = "💼 **Portefeuille IA** :\n"
    total = 0.0

    for asset, qty in capital.items():
        if qty <= 0:
            continue
        if asset != "USDT":
            price_str = get_price(asset)
            try:
                price = float(price_str.split("➤")[1].split()[0])
                value = qty * price
                total += value
                msg += f"• {asset}: {qty:.4f} → {value:.2f} USDT\n"
            except:
                msg += f"• {asset}: {qty:.4f} → ❌ Prix indisponible\n"
        else:
            total += qty
            msg += f"• USDT: {qty:.2f}\n"

    msg += f"\n📊 Valeur totale estimée : **{total:.2f} USDT**"
    await ctx.send(msg)

# ▶️ Démarrage
@bot.event
async def on_ready():
    print(f"🚀 Bot connecté : {bot.user.name}")
    print("📡 En attente des commandes IA")

bot.run(TOKEN)