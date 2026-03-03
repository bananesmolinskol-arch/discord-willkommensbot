import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# .env laden
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

WELCOME_CHANNEL_ID = 1476528505029394587
ROLE_ID = 1476528502999224333

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Eingeloggt als {bot.user}")


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    role = member.guild.get_role(ROLE_ID)

    if role:
        await member.add_roles(role)

    embed = discord.Embed(
        title="Willkommen!",
        description=f"Hey {member.mention}, schön dass du da bist!",
        color=discord.Color.green()
    )

    embed.set_thumbnail(url=member.display_avatar.url)

    await channel.send(embed=embed)


bot.run(TOKEN)
