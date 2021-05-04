import discord
import discord as d
import youtube_dl
from discord.ext import commands

class Music(commands.Cog):
  def __init__(self,bot):
    self.bot=bot
  
  @commands.command()
  async def join(self, ctx, channel):
    VoiceChannel = discord.utils.get(ctx.guild.voice_channels, name = channel)
    bot_voice = discord.utils.get(self.bot.voice_clients, guild= ctx.guild)
    if not bot_voice.is_connected():
      await VoiceChannel.connect()
   
  @commands.command()
  async def leave(self,ctx):
    bot_voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)
    if bot_voice.is_connected():
      await bot_voice.disconnect()
    else:
      await ctx.send("The bot is not connected to any voice channel.")


def setup(client):
  client.add_cog(Music(client)) 