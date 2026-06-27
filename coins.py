import discord
from discord.ext import commands
from discord import app_commands
import json
import random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


# ====== حط ID قناة الإعلانات هنا ======
AD_CHANNEL_ID = 0
# مثال:
# AD_CHANNEL_ID = 123456789012345678


try:
    with open("coins.json","r") as f:
        coins = json.load(f)
except:
    coins = {}


def save():
    with open("coins.json","w") as f:
        json.dump(coins,f)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot Online")


# ================= COINS =================


@bot.tree.command(name="balance", description="شوف Coins")
async def balance(interaction: discord.Interaction):

    uid = str(interaction.user.id)

    if uid not in coins:
        coins[uid] = 0

    await interaction.response.send_message(
        f"💰 عندك {coins[uid]} Coins"
    )



@bot.tree.command(name="daily", description="خذ Coins")
async def daily(interaction: discord.Interaction):

    uid = str(interaction.user.id)

    if uid not in coins:
        coins[uid] = 0

    amount = random.randint(50,200)

    coins[uid] += amount
    save()

    await interaction.response.send_message(
        f"🎁 ربحت {amount} Coins"
    )



@bot.tree.command(name="addcoins", description="إضافة Coins")
@app_commands.checks.has_permissions(administrator=True)
async def addcoins(
    interaction: discord.Interaction,
    member: discord.Member,
    amount:int
):

    uid = str(member.id)

    if uid not in coins:
        coins[uid] = 0

    coins[uid] += amount
    save()

    await interaction.response.send_message(
        "✅ تمت الإضافة"
    )



# ================= SHOP =================


class AdModal(discord.ui.Modal, title="📢 كتابة الإعلان"):

    text = discord.ui.TextInput(
        label="الإعلان",
        placeholder="اكتب إعلانك هنا...",
        style=discord.TextStyle.paragraph,
        max_length=1000
    )


    async def on_submit(self, interaction: discord.Interaction):

        channel = bot.get_channel(AD_CHANNEL_ID)


        if channel:

            await channel.send(
                f"📢 **إعلان جديد**\n\n"
                f"{self.text.value}\n\n"
                f"👤 {interaction.user.mention}"
            )


        await interaction.response.send_message(
            "✅ تم نشر إعلانك",
            ephemeral=True
        )




class ShopView(discord.ui.View):

    @discord.ui.button(
        label="📢 شراء إعلان - 50 Coins",
        style=discord.ButtonStyle.green
    )
    async def buy(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):


        uid = str(interaction.user.id)


        if uid not in coins:
            coins[uid] = 0


        if coins[uid] < 50:

            await interaction.response.send_message(
                "❌ ماعندكش 50 Coins",
                ephemeral=True
            )
            return


        coins[uid] -= 50
        save()


        await interaction.response.send_modal(
            AdModal()
        )



@bot.tree.command(name="shop", description="فتح المتجر")
async def shop(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🛒 متجر السيرفر",
        description="اختار الخدمة"
    )


    embed.add_field(
        name="📢 إعلان",
        value="💰 السعر: 50 Coins\nاضغط الزر تحت",
        inline=False
    )


    await interaction.response.send_message(
        embed=embed,
        view=ShopView()
    )
AD_CHANNEL_ID = 1515118563340324994

bot.run("MTUxNTEyMDY4OTMxNTg0NDI0OA.GoBXuX.pAJ0jmX-WweJsRlNUv7tWnD7FXTZ-RsTVjD_Sk")