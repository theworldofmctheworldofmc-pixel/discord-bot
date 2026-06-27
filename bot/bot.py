import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("hello!")

@bot.command()
async def hello(ctx):
    await ctx.send("سلام 👋")

bot.run("MTUxNTEyMDY4OTMxNTg0NDI0OA.GNgEMV.LfWEsLYl8tL7B_Q54JgMnt32Bb_H-QLNZ1YPYY")