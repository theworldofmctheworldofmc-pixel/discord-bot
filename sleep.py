import discord
from discord.ext import commands
import asyncio

TOKEN = "MTUxNTEyMDY4OTMxNTg0NDI0OA.GmAGUc.xNAnliKtGmNKz_OGkpWRpbzU4lURXhxEmHyejA"

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="&", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

while True:
    try:
        bot.run(TOKEN)
    except Exception as e:
        print(f"Crash: {e}")
        print("🔄 إعادة التشغيل بعد 5 ثوان...")
        asyncio.run(asyncio.sleep(5))

        