import discord
from discord.ext import commands
class Levels(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

def setup(client):
    client.add_cog(Levels(client))