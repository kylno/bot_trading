# discord_switch.py
import discord
from discord.ext import commands
import json

TOKEN = "TON_TOKEN_ICI"  # 🔐 Remplace par ton vrai token bot Discord

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

CONFIG_PATH = "config_mode.json"

def changer_mode(auto: bool):
    with open(CONFIG_PATH, "w") as f:
        json.dump({"auto_mode": auto}, f, indent=2)

@bot.command()
async def mode(ctx, arg):
    if arg.lower() == "auto":
        changer_mode(True)
        await ctx.send("✅ Mode AUTO activé. L’IA prend le contrôle 🤖")
    elif arg.lower() == "manuel":
        changer_mode(False)
        await ctx.send("🛑 Mode MANUEL activé. Observation uniquement 🧠")
    else:
        await ctx.send("❓ Utilise : `!mode auto` ou `!mode manuel`")

bot.run(TOKEN)