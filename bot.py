import os
import discord
from discord import app_commands

TOKEN = os.getenv("TOKEN")

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()


client = MyClient()


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.tree.command(
    name="echo",
    description="Send a message as the app"
)
@app_commands.describe(
    message="What you want the app to say"
)
async def echo(interaction: discord.Interaction, message: str):

    # Hidden confirmation for you
    await interaction.response.send_message(
        "Sent!",
        ephemeral=True
    )

    # Send the message publicly in servers
    if interaction.guild:
        await interaction.followup.send(
            message,
            ephemeral=False
        )

    # Send the message in DMs
    else:
        await interaction.followup.send(
            message,
            ephemeral=False
        )


client.run(TOKEN)
