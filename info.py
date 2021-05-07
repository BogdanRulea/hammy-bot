import discord
import discord as d
from discord.ext import commands

class Info(commands.Cog):
  def __init__(self,bot):
    self.bot = bot
  
  @commands.command()
  async def commands_list(self,ctx):
   mbed = d.Embed(title = "Commands list:", description="**?info** - bot description\n**?spy** - creepy hamster that watches you\n**?inspire** - motivational quote\n**?hug + [@ user]** - hug someone you mention\n**?howgay** - shows you how gay you are\n**?auctions + [@ user]** - ping someone you mention to check auctions\n**?sus + [@ user]** - check if a user is an impostor or not\n**?drink** - trigger I will drink to that message\n**?rps + {choice}** - Rock Paper Scissors game\n**?punch + [@ user]** - punch someone you mention\n**?slap + [@ user]** - slap someone you mention\n**?hamster** - show a cute hamster gif\n**?coin** - flip a coin\n**?bonk + [@user id]** - bonk someone\n**?howstinkyis + [@ user]** - Stinky meter\n**?boop + [@ user]** - boop someone\n**?inrole + [role id]** - gives you the number of people with a specified role\n**?serverinfo** - show server information\n**?uptime** - shows bot's uptime\n**?userinfo + [@user id] (optional)** - show user's info",colour=discord.Colour(0xff9966))
   await ctx.channel.send(embed=mbed)
  
  @commands.command()
  async def staffcmds(self,ctx):
    if ctx.message.author.guild_permissions.manage_messages:
     mbed = d.Embed(title = "Commands list:", description="**?hmyeat + [number]** - purge the given number of messages from the channel (Command for middleman, mod+)\n**?announce + follow the requirements** - send the announcement/question to the given channel (Command for staff members only)\n**?ben + [id or @ user] + reason **- ben members\n**?case_open + [judge id/mention] + [member id/mention]** - create a channel for member's case\n**?case_closed + [channel]** - delete the specified channel and send the transcript in the channel where the command was appealed\n **?witness + [@used id]** - add/kick witnesses from interrogation channels\n **?reminder + [number][s or m or h or d] + reason(optional)** - set a reminder for a specified reason\n**?poll + [channel] + \"question\" + [\"Options\"] **- create a poll in the specified channel with the given options (if you have only 2 options, yes and no, then it will create a yes and no pool otherwise it will create a poll with max. 10 options) - the question and all options have to be between \"\" -** Ex: ?poll #channel \"question\" \"option1\" \"option2\"**\n**?poll_res + [poll id]** - return the results of the given poll\n**?bump** - !d bump reminder",colour=discord.Colour(0xff9966))
     await ctx.channel.send(embed=mbed)
    else:
     await ctx.channel.send("> You don't have the permissions to use this command.")

  @commands.command()
  async def info(self,ctx):
    mbed = d.Embed(title = "Bot info", description = "Hi i am Hammy bot!\nMy creator is Hammy(that stupid dude that likes hamsters).\nI was coded in Python, as a personal project(for fun).\nMy developer is a lazy ass and i am sorry if i don't have that many features.\nMy purpose in this server is to entertain people and i am trying my best to be useful sometimes.\nMore updates will come soon.\nLove you all! <:hammyheart:796027824494477384>",colour = discord.Colour(0xff9966))
    mbed.set_thumbnail(url = str(self.bot.user.avatar_url))
    await ctx.channel.send(embed = mbed)
  
  @commands.command()
  async def music(self, ctx):
    mbed = d.Embed(title = "(Beta)Music commands:", description = "**?join** - add the bot in the voice channel\n**?leave** - kick the bot from the voice channel\n**?play + {song name}** - play a song if there is no queue otherwise it will add the song to the song queue\n**?queue** - shows the songs queue\n**?skip** - skip the current song\n**?pause** - pause the player\n**?resume** - start the player again\n**?volume + {float number}(0-100 range)** - change the volume of the player\n**?remove + {index}** - remove the song from the queue with the specified index\n**?stop** - stop the player\n**?loop** - enable/disable the loop for the current song",color = 0xff9966)
    mbed.set_thumbnail(url = str(ctx.guild.icon_url))
    await ctx.send(embed = mbed)
def setup(client):
  client.add_cog(Info(client))