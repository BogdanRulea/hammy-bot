import discord 
from discord.ext import commands
import random
import discord as d

class Games(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    
  @commands.command(name = "coin",description = "flip a coin")
  async def coin(self,ctx):
   mbed = d.Embed(title = '**Flip a coin**', color = 0xff9966)
   mbed.add_field(name = "User:", value = ctx.message.author.mention, inline = True)
   mbed.add_field(name = "Coin:", value = random.choice(["tails","heads"]), inline = True)
   mbed.set_thumbnail(url = str(ctx.author.avatar_url))
   await ctx.send(embed = mbed)
  
  @commands.command(name = "rps", description = "Rock Paper Scissors game")
  async def rps(self,ctx, choice):
   rock_paper_scissor = ["rock", "paper", "scissors"]
   if not choice.lower() in rock_paper_scissor:
     await ctx.send("Choice invalid. Please try again.")
   else:
     rand_choice = random.choice(rock_paper_scissor)
     mbed = d.Embed(title = "Rock Paper Scissors Game",color = 0xff996)
     mbed.set_thumbnail(url = str(ctx.guild.icon_url))
     mbed.add_field(name = f"{ctx.author.name}'s choice:", value = choice, inline = True)
     mbed.add_field(name = "Bot's choice:", value = rand_choice, inline = True)
     if choice.lower() == "rock":
       if rand_choice == "paper":
         mbed.add_field(name = "Result:", value = "Bot won.",inline=False)
       elif rand_choice == "scissors":
        mbed.add_field(name = "Result:", value = f"{ctx.author.name}  won.",inline=False)
       else:
        mbed.add_field(name = "Result:", value = f"You both choose {rand_choice}. Tie.",inline=False)
     if choice.lower() == "paper":
       if rand_choice == "paper":
         mbed.add_field(name = "Result:", value = f"You both choose {rand_choice}. Tie.",inline=False)
       elif rand_choice == "scissors":
         mbed.add_field(name = "Result:", value = f"Bot won.",inline=False)
       else:
         mbed.add_field(name = "Result:", value = f"{ctx.author.name}  won.",inline=False)
     if choice.lower() == "scissors":
       if rand_choice == "rock":
         mbed.add_field(name = "Result:", value = "Bot won.",inline=False)
       elif rand_choice == "paper":
         mbed.add_field(name = "Result:", value = f"{ctx.author.name}  won.",inline=False)
       else:
         mbed.add_field(name = "Result:", value = f"You both choose {rand_choice}. Tie.",inline=False)
   await ctx.send(embed = mbed)

  @commands.command(name = "dice", description = "roll a dice")
  async def dice(self,ctx):
    mbed = d.Embed(title = "Dice",color = 0xff9966)
    mbed.add_field(name = "User", value = str(ctx.author.mention),inline = True)
    mbed.add_field(name = "Your number: ", value = str(random.choice(range(1,6))), inline = True)
    await ctx.send(embed = mbed)
  
  @commands.command(description = "This command shows you the pp size")
  async def pp(self, ctx, member : discord.Member = None):
    if member == None:
      member = ctx.author
    mbed = d.Embed(title = f"{member.name}'s pp size:", description = "8"+ f"".join('=' for i in range(random.randrange(0,15))) + "D",color = 0xff9966)
    await ctx.send(embed = mbed)
  
  @commands.command(description = "This command shows you the nerd level")
  async def nerd(self,ctx, member : discord.Member = None):
    if member == None:
      member = ctx.author
    
    mbed = d.Embed(title = f"{member.name}'s nerd level:", description = f"You are {random.randrange(0,100)}/100 nerd.", color = 0xff9966)
    await ctx.send(embed = mbed)
  
  @commands.command(description = "This command shows you the simp rate")
  async def simp(self,ctx, member : discord.Member = None):
    if member == None:
      member = ctx.author
    
    mbed = d.Embed(title = f"{member.name}'s simp rate:", description = f"You are {random.randrange(0,100)}/100 simp.", color = 0xff9966)
    await ctx.send(embed = mbed)
  
  @commands.command(description = "This command shows you the alchy level")
  async def alchy(self,ctx, member : discord.Member = None):
    if member == None:
      member = ctx.author
    mbed = d.Embed(title = f"{member.name}'s alchy level:", description = f"You are {random.randrange(0,100)}/100 alchy.", color = 0xff9966)
    await ctx.send(embed = mbed)
  
  @commands.command(description = "This command shows you the waifu level")
  async def waifu(self,ctx, member : discord.Member = None):
    if member == None:
      member = ctx.author
    mbed = d.Embed(title = f"{member.name}'s waifu level:", description = f"You are {random.randrange(0,100)}/100 waifu. <:pepeblush:814708544921927690>", color = 0xff9966)
    await ctx.send(embed = mbed)
  
  @commands.command(name = "8ball", description ="Troll responses.")
  async def _8ball(self,ctx,*,question : str):
    random_response = ["I don't care", "Maybe or maybe not", "I don't know 4head", "No, ofc not", "Yes and what about it", "Idk but i know you are dumb", "mayhaps", "Who told you that?","Idk, stay away from me", "Idk and i don't care.", "I don't talk to stupid ppl.", "Yes, this is true my love.", "Who are you to ask this question?","Yes, don't tell anyone.", "Sure, why not.", "Yes, definitely yes."]
    await ctx.reply(f"🎱{random.choice(random_response)}")

def setup(client):
  client.add_cog(Games(client))