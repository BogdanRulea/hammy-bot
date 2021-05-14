import discord
import discord as d
import math
import discord, time, datetime
from discord.ext import commands
import platform
import DiscordUtils
import json
class Info(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  start_time=time.time()

  @commands.command(name = "stats",aliases = ["info","uptime"], description = "Bot info and statistics")
  async def stats(self,ctx):
    mbed = d.Embed(title = "Bot info", description = "Hi i am Hammy bot!\nMy creator is Hammy(that stupid dude that likes hamsters).\nI was coded in Python, as a personal project(for fun).\nMy developer is a lazy ass and i am sorry if i don't have that many features.\nMy purpose in this server is to entertain people and i am trying my best to be useful sometimes.\nMore updates will come soon.\nLove you all! <:hammyheart:796027824494477384>",colour = discord.Colour(0xff9966))
    mbed.set_thumbnail(url = str(self.bot.user.avatar_url))
    pyversion = platform.python_version()
    dpyversion = discord.__version__
    serverCount = len(self.bot.guilds)
    memberCount = len(set(self.bot.get_all_members()))
    mbed.add_field(name = "Python Version: ", value = pyversion)
    mbed.add_field(name = "discord.py Version: ", value = dpyversion)
    mbed.add_field(name = "Servers Count: ", value = serverCount)
    mbed.add_field(name = "Members Count: ", value = memberCount)
    current_time = time.time()
    difference = int(round(current_time - self.start_time))
    text = str(datetime.timedelta(seconds=difference))
    mbed.add_field(name="Uptime", value=text)
    mbed.set_footer(text=f"{self.bot.user.name}")
    await ctx.channel.send(embed = mbed)
  
  @commands.command(name = 'help', aliases = ["h",'commands'], description = "Hammy bot commands")
  async def help(self,ctx):
    
    cogs = [c for c in self.bot.cogs.keys()]
    cogs.remove('Levels')
    embeds = []

    for cog in cogs:
      commandList= ""
      for command in self.bot.get_cog(cog).walk_commands():
        if command.hidden:
          continue
        commandList += f"``{command.name}`` - *{command.description}*\n"
        if len(command.aliases) > 0:
          commandList+="**Aliases: **" + ", ".join(command.aliases) + "\n\n"

      help_mbed=d.Embed(title = "Help command!(beta)", color = 0xff9966)
      #help_mbed.add_field(name = "Commands prefix:", value = )
      help_mbed.add_field(name=cog, value=commandList, inline = False)
      embeds.append(help_mbed)

    paginator = DiscordUtils.Pagination.CustomEmbedPaginator(ctx,auto_footer = True, remove_reactions= True, timeout = 60)
    paginator.add_reaction('↩️', "first")
    paginator.add_reaction('⬅️', "back")
    paginator.add_reaction('🛑', "lock")
    paginator.add_reaction('➡️', "next")
    paginator.add_reaction('↪️', "last")

    await paginator.run(embeds)

  @commands.command(description = "change the bot prefix(admin+ only)")
  @commands.has_permissions(administrator = True)
  async def prefix(self,ctx, prefix = "?"):
    with open("prefixes.json", "r") as f:
      prefixes = json.load(f)
    
    prefixes[str(ctx.guild.id)] = prefix

    with open("prefixes.json", "w") as f:
      json.dump(prefixes, f, indent = 4)
    await ctx.send("My prefix has been changed to {}".format(prefix)) 

  
def setup(client):
  client.add_cog(Info(client))