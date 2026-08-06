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


@bot.tree.command(name="echo", description="Make the bot say something")
@app_commands.describe(message="Message to send")
async def echo(interaction: discord.Interaction, message: str):

    # Hidden message only you see
    await interaction.response.send_message(
        "Sent!",
        ephemeral=True
    )

    # Public message from the bot
    await interaction.followup.send(
        message,
        ephemeral=False
    )


bot.run(TOKEN)
