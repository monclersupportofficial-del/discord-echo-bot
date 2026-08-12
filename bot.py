import discord
from discord import app_commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.none()
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced.")

client = MyClient()

@client.tree.command(
    name="echo",
    description="Send a message as the app"
)
@app_commands.allowed_installs(guilds=False, users=True)
@app_commands.allowed_contexts(
    guilds=False,
    dms=True,
    private_channels=True
)
@app_commands.describe(message="The message to send")
async def echo(interaction: discord.Interaction, message: str):

    # Private confirmation
    await interaction.response.send_message(
        "Sent!",
        ephemeral=True
    )

    # Public message
    await interaction.channel.send(message)
    
client.run(TOKEN)
