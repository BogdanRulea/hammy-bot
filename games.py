import discord 
from discord.ext import commands
import random
import discord as d

class Games(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
    
  @commands.command()
  async def coin(self,ctx):
   mbed = d.Embed(title = '**Flip a coin**', color = 0xff9966)
   mbed.add_field(name = "User:", value = ctx.message.author.mention, inline = True)
   mbed.add_field(name = "Coin:", value = random.choice(["tails","heads"]), inline = True)
   mbed.set_thumbnail(url = str(ctx.author.avatar_url))
   await ctx.send(embed = mbed)
  
  @commands.command()
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

  @commands.command()
  async def dice(self,ctx):
    mbed = d.Embed(title = "Dice",color = 0xff9966)
    mbed.add_field(name = "User", value = str(ctx.author.mention),inline = True)
    mbed.add_field(name = "Your number: ", value = str(random.choice(range(1,6))), inline = True)
    await ctx.send(embed = mbed)
  

def setup(client):
  client.add_cog(Games(client))