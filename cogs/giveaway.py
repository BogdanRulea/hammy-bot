import discord
from discord.ext import commands
import random

class Giveaway(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.command(name = "roll", description = "This command gives you a random ticket from 0 to 100.")
    async def _roll(self,ctx,channel : discord.TextChannel = None):
        if channel == None:
            await ctx.send(f"{ctx.author.mention} your ticket is: **{random.randrange(1,100)}**.")
        else:
            channel = self.bot.get_channel(channel.id)
            await channel.send(f"{ctx.author.mention} your ticket is: **{random.randrange(1,100)}**.")
            await ctx.send(f"**Your ticket has been sent to {channel.mention}**")


def setup(client):
    client.add_cog(Giveaway(client))