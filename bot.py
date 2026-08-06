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
    description="Send a message"
)
@app_commands.describe(message="Message to send")
async def echo(interaction: discord.Interaction, message: str):

    await interaction.response.send_message(
        "Sent!",
        ephemeral=True
    )

    await interaction.followup.send(
        message
    )


client.run(TOKEN)
