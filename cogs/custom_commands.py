import discord 
from discord.ext import commands
import random
import discord as d
import json
import requests

class Custom_Commands(commands.Cog):
  def __init__(self,bot):
    self.bot = bot

  @commands.command(name = "boop", description = "boop someone")
  async def boop(self,ctx, member: discord.Member = None):
   if member is None:
     member = ctx.author
   await ctx.channel.send(f"{member.mention} boop boop boop\nhttps://media.giphy.com/media/SYLvjCEtBClsS2QePl/giphy.gif")

  @commands.command(name = "hug", description = "hug someone you mention")
  async def hug(self,ctx, member: discord.Member = None):
    if member is None:
      member = ctx.author
      await ctx.send(ctx.author.mention + "you hugged yourself weirdo")
    else:
      await ctx.channel.send(ctx.author.mention + " gave you a hug " + member.mention + "\nhttps://media.giphy.com/media/EvYHHSntaIl5m/giphy.gif")

  @commands.command(name = "drink",description = "trigger I will drink to that message")
  async def drink(self,ctx):
    await ctx.send('I will drink to that!' + '\nhttps://media.giphy.com/media/g9582DNuQppxC/giphy.gif')

  @commands.command(name = "sus",description = "check if a user is an impostor or not")
  async def sus(self,ctx, member: discord.Member = None):
    if member is None:
      member = ctx.author
    impostor = random.choice(["you are sus", "you are not sus"])
    if impostor == "you are not sus":
        await ctx.channel.send( member.mention + ' ' + impostor +"\nhttps://media.giphy.com/media/26gsj4w562sneqcaQ/giphy.gif")

    else:
        await ctx.send(member.mention + ' ' + impostor + "\nhttps://media.giphy.com/media/Huo7qbHGNnXUVoRYL9/giphy.gif")

  @commands.command(name = "bonk",description = "bonk someone")
  async def bonk(self,ctx, member: discord.Member = None):
   if member is None:
     member = ctx.author
   await ctx.send(f"{member.mention} you got bonked\nhttps://media.giphy.com/media/30lxTuJueXE7C/giphy.gif")
  
  
  @commands.command(name = "spy",description = "creepy hamster that watches you")
  async def spy(self,ctx):
    await ctx.send( f"I am watching you " + '\n https://media.giphy.com/media/pm4VOSkAgkj3q/giphy.gif')
  
  @commands.command(name = "slap",description = "slap someone you mention")
  async def slap(self,ctx, member: discord.Member = None):
    if member is None:
      member = ctx.aucthor
      await ctx.send(member.mention +" Are you ok?")
    else:  
     await ctx.send(member.mention +" You got slapped\nhttps://media.giphy.com/media/u8maN0dMhVWPS/giphy.gif"
    )

  @commands.command(name = "howgay",description = "shows you how gay you are")
  async def howgay(self,ctx):
   mbed = d.Embed(title = "How gay are you?",description = f"{ctx.author.mention} you are {random.randrange(1,100)}% gay ??????????????", color = 0xff9966) 
   mbed.set_thumbnail(url=str(ctx.author.avatar_url))
   await ctx.send(embed = mbed)

  @commands.command(name = "hamster",description = "show a cute hamster gif")
  async def hamster(self,ctx):
   await ctx.send(f"{ctx.message.author.mention}\nhttps://media.giphy.com/media/P4EO3u0apt3PO/giphy.gif")
  
  @commands.command(name = "howstinkyis",description = "Stinky meter")
  async def howstinkyis(self,ctx, member : discord.Member = None):
   if member is None:
     member = ctx.author
   stink = random.randrange(1,100)
   if stink<=20 :
     await ctx.channel.send(f"Stinky meter: {stink}% stink.\nBetter take a shower,{member.mention}!\nhttps://media.giphy.com/media/3og0IBBXyY574s05Pi/giphy.gif")
   elif stink<=50 and stink>=21:
     await ctx.channel.send(f"Stinky meter: {stink}% stink.\nYou stink like a skunk, {member.mention}\nhttps://media.giphy.com/media/3orifi2I4IHETUuBGg/giphy.gif")
   elif stink<=90 and stink>=51:
     await ctx.channel.send(f"Stinky meter: {stink}% stink.\nYou stink like you are made of farts, {member.mention}.\nhttps://media.giphy.com/media/TIWrHYuuOKc3j90Ylm/giphy.gif")
   else:
     await ctx.channel.send(f"Stinky meter: {stink}% stink.\nSquishy is that you? {member.mention}\nhttps://media.giphy.com/media/LdF19xcqxH1Be/giphy.gif")

  @commands.command(name = "ben", description = "ben members")
  async def ben(self,ctx, member : discord.Member, *,message):
   if ctx.author.guild_permissions.manage_messages:
     await ctx.message.channel.purge(limit = 1)
     await ctx.send(f"{member.name} has been benned.BYE!")
     channel = await member.create_dm()
     mbed = d.Embed(Title = 'Warning', description = f"{member} you have been benned in {ctx.guild.name} for the following reason: {message}")
     await channel.send(embed = mbed)
   else:
     ctx.send('You do not have the permissions to use this command')
  
  @commands.command(name = "wern", description = "wern members")
  async def wern(self, ctx, member : discord.Member, *, message):
    if ctx.author.guild_permissions.manage_messages:
      await ctx.message.channel.purge(limit= 1)
      await ctx.send(f"{member.name} has been werned!")
      channel = await member.create_dm()
      mbed = d.Embed(title = "Warning", description = f"{member} you have been werned in {ctx.guild.name} for the following reason: {message}\nThis is your 69th warning that you got, one more mistake and you will be banned!")
      await channel.send(embed = mbed)
    else: 
      await ctx.send("You do not have the permissions to use this command")



def setup(client):
 client.add_cog(Custom_Commands(client))