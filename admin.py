import discord
from discord.ext import commands
from discord import app_commands

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    await bot.tree.sync()
    print("✅ Bot Online")


# ترحيب
@bot.event
async def on_member_join(member):
    if member.guild.system_channel:
        await member.guild.system_channel.send(
            f"👋 مرحبا {member.mention}"
        )


# Slash ping
@bot.tree.command(name="ping", description="فحص البوت")
async def ping(interaction:discord.Interaction):
    await interaction.response.send_message(
        "🏓 البوت خدام"
    )


# مسح
@bot.tree.command(name="clear", description="مسح رسائل")
@app_commands.checks.has_permissions(manage_messages=True)
async def clear(
    interaction:discord.Interaction,
    amount:int
):
    await interaction.channel.purge(limit=amount)

    await interaction.response.send_message(
        f"🧹 تم مسح {amount}",
        ephemeral=True
    )


# إعلان
@bot.tree.command(name="announce", description="إعلان")
@app_commands.checks.has_permissions(administrator=True)
async def announce(
    interaction:discord.Interaction,
    message:str
):
    await interaction.channel.send(
        f"📢 **إعلان**\n\n{message}"
    )

    await interaction.response.send_message(
        "✅ تم",
        ephemeral=True
    )


# ميوت
@bot.tree.command(name="mute", description="ميوت عضو")
@app_commands.checks.has_permissions(manage_roles=True)
async def mute(
    interaction:discord.Interaction,
    member:discord.Member
):
    role = discord.utils.get(
        interaction.guild.roles,
        name="Muted"
    )

    if role:
        await member.add_roles(role)
        await interaction.response.send_message(
            "🔇 تم الميوت"
        )
    else:
        await interaction.response.send_message(
            "دير رتبة اسمها Muted"
        )


bot.run("MTUxNTEyMDY4OTMxNTg0NDI0OA.GoBXuX.pAJ0jmX-WweJsRlNUv7tWnD7FXTZ-RsTVjD_Sk")