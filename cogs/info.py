import discord
import discord as d
import math
from discord.ext import commands
import DiscordUtils
class Info(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command(name = "info", description = "Bot info")
  async def info(self,ctx):
    mbed = d.Embed(title = "Bot info", description = "Hi i am Hammy bot!\nMy creator is Hammy(that stupid dude that likes hamsters).\nI was coded in Python, as a personal project(for fun).\nMy developer is a lazy ass and i am sorry if i don't have that many features.\nMy purpose in this server is to entertain people and i am trying my best to be useful sometimes.\nMore updates will come soon.\nLove you all! <:hammyheart:796027824494477384>",colour = discord.Colour(0xff9966))
    mbed.set_thumbnail(url = str(self.bot.user.avatar_url))
    await ctx.channel.send(embed = mbed)
  
  @commands.command(name = 'help', aliases = ["h",'commands'], description = "Hammy bot commands")
  async def help(self,ctx,cog = '1'):
    help_mbed=d.Embed(title = "Help command!(beta)", color = 0xff9966)
    cogs = [c for c in self.bot.cogs.keys()]
    cogs.remove('Levels')
    total_pages = len(cogs)
    cog = int(cog)
    if cog > total_pages or cog<1:
      await ctx.send(f"Invalid page number: {cog}. Please pick from {total_pages} pages. You can you use the default **help** command that will show the first page.")
    
    for cog in cogs:
      commandList= ""
      for command in self.bot.get_cog(cog).walk_commands():
        commandList += f"**{command.name}** - *{command.description}*\n"
      commandList+='\n'
      help_mbed.add_field(name=cog, value=commandList, inline = False)
    
    await ctx.send(embed = help_mbed)



    """
    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx)
    paginator.add_reaction('⏮️', "first")
    paginator.add_reaction('⏪', "back")
    paginator.add_reaction('🔐', "lock")
    paginator.add_reaction('⏩', "next")
    paginator.add_reaction('⏭️', "last")
    """

  
def setup(client):
  client.add_cog(Info(client))