import os
import discord
from discord.ext import commands
from discord import app_commands

TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(
    name="echo",
    description="Repeats your message privately"
)
@app_commands.describe(
    message="The message you want the bot to repeat"
)
async def echo(interaction: discord.Interaction, message: str):
    await interaction.response.send_message(
        message,
        ephemeral=True
    )

bot.run(TOKEN)
