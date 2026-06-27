import discord
from discord import app_commands

TOKEN = "YOUR_NEW_BOT_TOKEN"

intents = discord.Intents.default()
intents.members = True

class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("✅ Slash Commands Synced")

bot = MyBot()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="dm", description="إرسال رسالة خاصة إلى عضو")
@app_commands.checks.has_permissions(administrator=True)
@app_commands.describe(
    member="اختر العضو",
    message="اكتب الرسالة"
)
async def dm(
    interaction: discord.Interaction,
    member: discord.Member,
    message: str
):
    try:
        await member.send(message)
        await interaction.response.send_message(
            f"✅ تم إرسال الرسالة إلى {member.mention}",
            ephemeral=True
        )
    except discord.Forbidden:
        await interaction.response.send_message(
            "❌ لا أستطيع إرسال DM لهذا العضو.",
            ephemeral=True
        )
bot.run("MTUxNTEyMDY4OTMxNTg0NDI0OA.GoBXuX.pAJ0jmX-WweJsRlNUv7tWnD7FXTZ-RsTVjD_Sk")