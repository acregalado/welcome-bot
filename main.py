import discord
from discord.ext import commands
import os
from keep_alive import keep_alive
from zoneinfo import ZoneInfo

TOKEN = os.getenv("DISCORD_TOKEN")

WELCOME_CHANNEL_NAME = "welcome"
CUSTOM_IMAGE_URL = "https://i.imgur.com/st7BRwj.png"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name=WELCOME_CHANNEL_NAME)
    if channel:
        pst_time = member.joined_at.astimezone(ZoneInfo("America/Los_Angeles"))
        join_time = pst_time.strftime("%I:%M %p").lstrip("0")
        embed = discord.Embed(
            title=f"☕️ Welcome to {member.guild.name}!",
            description=(
                f"Hey {member.display_name}, thanks for joining the coffeehits discord server!"
                " Let us know what brought you here in <#1399209775698546798>"
                " to gain access to the rest of it!"
            ),
            color=discord.Color.blue()
        )
        embed.set_author(
            name=member.display_name,
            icon_url=member.avatar.url if member.avatar else member.default_avatar.url
        )
        embed.set_thumbnail(url=member.avatar.url if member.avatar else member.default_avatar.url)
        embed.set_image(url=CUSTOM_IMAGE_URL)
        embed.set_footer(text=f"You are member #{len(member.guild.members)} | Joined at {join_time} PST")
        await channel.send(embed=embed)

keep_alive()
bot.run(TOKEN)
