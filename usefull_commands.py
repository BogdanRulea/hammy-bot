import discord
import asyncio
import io
import discord, datetime, time
import os
import random
import discord as d
from discord.ext import commands

class Useful_Commands(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def bump(self,ctx):
   await ctx.send("Bump done?(Yes or No)")
   def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel
   msg = await self.bot.wait_for('message',check = check)
   if msg.content.lower() == 'yes':
    await ctx.send("Ok i will remind you to !d bump again in 2 hours.")
    await asyncio.sleep(2*60*60)
    await ctx.send("Two Hour Reminder: **Please use the !d bump command every 2 hours or so.** @here\n> This command puts us at the top of the leaderboard of a \"Discord server search\" website to increase our chances of getting more members! Only one person can use this command every 2 hours.")
   else:
    await ctx.send("Ok i will wait for next d bump.")
  
  @commands.command()
  async def inrole(self, ctx, role : discord.Role):
   rol = ctx.guild.get_role(role.id)
   memberlist = [] 
   if len(rol.members) <= 50:
    for r in rol.members:
      memberlist.append(f"{r.display_name}#{r.discriminator}")
    mbed = d.Embed(title = f"**{len(role.members)} members have {role} role:**",description = "\n".join(memberlist),colour=discord.Colour(0xff9966))
    mbed.set_thumbnail(url=str(ctx.guild.icon_url))
    await ctx.channel.send(embed = mbed)
   else:
    await ctx.channel.send(f"> **{len(role.members)} members have {role} role:**\n> **TOO MANY NAMES TO SHOW**")
  
  @commands.command()
  async def announce(self,ctx):
   if ctx.author.guild_permissions.manage_messages:

    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel
    
    await ctx.channel.send("**Do you want to use this command for wwyd purpose or any other announcement?(type one of this answers wwyd/others)**")

    purpose = await self.bot.wait_for("message", check = check)

    """
    WWYD CHOICE
    """
    if purpose.content.lower() == "wwyd":
      await ctx.channel.send("**Now type the channel where you want to post the question.**")
      try:
       cnel = await self.bot.wait_for("message", check = check)

       channel_id = cnel.channel_mentions[0].id

       channel = self.bot.get_channel(channel_id)
       await ctx.send("**Is this a select an answer question or a type your own question? Type one of the following**: **SELECT/TYPE**")

       CHOICE = await self.bot.wait_for('message', check=check)

       if CHOICE.content.lower()=="type":
          await ctx.channel.send("**Now type the wwyd question.(Don't forget to add '?')**\n **No bold needed!!!**")
       
          mess = await self.bot.wait_for("message", check=check)
      
          await channel.send(f"**Question: {mess.content}**\nThis is an open ended question. Answer in as many or as little words as you like. If you like someone's answer, be sure to <:star:821851035928231966> it!\nPost by {ctx.author.name}")
          mbed = d.Embed(title = "Success", description = f"The announcement was successfully posted in {channel.mention}.",)
          mbed.set_thumbnail(url = str(ctx.guild.icon_url))
          await ctx.send(embed = mbed)
       elif CHOICE.content.lower()=="select":
         await ctx.channel.send("**Now type the wwyd question.(Don't forget to add '?')**\n **No bold needed!!!**")
       
         mess = await self.bot.wait_for("message", check=check)
      
         await channel.send(f"**Question: {mess.content}**\nPick one of the options and explain why’d you choose it over the other(s). If you like someone’s answer, be sure to <:star:821851035928231966> it!\nPost by {ctx.author.name}")
         mbed = d.Embed(title = "Success", description = f"The announcement was successfully posted in {channel.mention}.",colour=discord.Colour(0xff9966))
         mbed.set_thumbnail(url = str(ctx.guild.icon_url))
         await ctx.send(embed = mbed)
       else:
         await ctx.send("**Choice unavailable, please try again!**")
      except IndexError:
        await ctx.send("**> This is not a valid channel**")

      """
       others choice
       """  
    elif purpose.content.lower() == "others":
      await ctx.channel.send("**Now type the channel where you want to post the question.**")
      try:
        cnel = await self.bot.wait_for("message", check = check)

        channel_id = cnel.channel_mentions[0].id

        channel = self.bot.get_channel(channel_id)
        await ctx.channel.send("**Now type the announcement.**")

        mess = await self.bot.wait_for("message", check = check)

        await channel.send(f"**Announcement:**\n{mess.content}\nAnnouncement by {ctx.author.name}.")
        mbed = d.Embed(title = "Success", description = f"The announcement was successfully posted in {channel.mention}.",colour=discord.Colour(0xff9966))
        mbed.set_thumbnail(url = str(ctx.guild.icon_url))
        await ctx.send(embed = mbed)
      except IndexError:
        await ctx.send("**> This is not a valid channel**")
    else:
     await ctx.channel.send("**Choice unavailable please try again.**")

    
   else:
    await ctx.channel.send("**You don't have the permissions to post a wwyd.**")

  @commands.command()
  async def reminder(self,ctx, time, *, remind_me = None):
   if ctx.author.guild_permissions.manage_messages:
    user = ctx.message.author
    mbed = d.Embed(color = 0xff9966)
    mbed.set_footer(text = "If you have any suggestions or bug report let Hammy know", icon_url = str(self.bot.user.avatar_url))
    seconds = 0;
    DM = await user.create_dm()
    if remind_me is None:
     mbed.add_field(name = "Warning", value = "Please specify what do you want me to remind you about.")
    if time.lower().endswith("d"):
     seconds += int(time[:-1]) * 60 * 60 * 24
     counter = f"{seconds // 60 // 60 // 24} days"
    if time.lower().endswith("h"):
     seconds += int(time[:-1]) * 60 * 60
     counter = f"{seconds // 60 // 60} hours"
    elif time.lower().endswith("m"):
     seconds += int(time[:-1]) * 60
     counter = f"{seconds // 60} minutes"
    elif time.lower().endswith("s"):
     seconds += int(time[:-1])
     counter = f"{seconds} seconds"
    if seconds == 0:
     mbed.add_field(name = "Warning", value = "Please specify a proper duration.")
    elif seconds > 7776000:
     mbed.add_field(name = "Warning", value = "You can set the reminder for up to 90 days.")
    else:
     mbed2 = d.Embed(title = "Reminder:", description = f"Ok, I will remind you about **{remind_me}** in {counter}", color = 0xff9966)
     await ctx.send(embed = mbed2)
     await asyncio.sleep(seconds)
     mbed3 = d.Embed(title = "Reminder:", description = f"Hi {ctx.author.mention}, you asked me to remind you about **{remind_me}** {counter} ago.", color = 0xff9966)
     await DM.send(embed = mbed3)
    await DM.send(embed = mbed)
   else:
    await ctx.send("You don't have the permissions to use this command.")
  
  @commands.command()
  async def poll(self,ctx, channel : discord.TextChannel, question : str, *options :str):
   if ctx.author.guild_permissions.manage_messages:
     if len(options) <=1:
       await ctx.send("**You need more that 1 option to create a pool.**")
       return 
     if len(options) >10:
       await ctx.send("**This command doesn't support more than 10 options.**")
       return
     if len(options) == 2 and options[0].lower() == 'yes' and options[1].lower() == 'no':
       reactions = ['✅', '❌']
     else:
       reactions = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣', '🔟']
     description = []
     for x, option in enumerate(options):
      description += f'\n{reactions[x]} {option}'
     mbed = d.Embed(title = question, description = ''.join(description), color = 0xff9966)
     mbed.set_thumbnail(url = str(ctx.guild.icon_url))

     chan = self.bot.get_channel(channel.id)
     react_message = await chan.send(embed = mbed)
     mbed.set_footer(text = f"Author: {ctx.message.author.name}/Poll ID: {react_message.id}")
     mbed2 = d.Embed(title = "Poll Created", description = f"{ctx.message.author.mention} your poll has been posted in {channel.mention}")
     await ctx.send(embed = mbed2)
     await react_message.edit(embed = mbed)
     for reaction in reactions[:len(options)]:
       await react_message.add_reaction(reaction)
     
   else:
    ctx.send("**You don't have the permissions to use this command.**")


  @commands.command(pass_context = True)
  async def poll_res(self,ctx, id):
   if ctx.author.guild_permissions.manage_messages:
    poll_msg = await ctx.fetch_message(id)
    if not poll_msg.embeds:
      return
    mbed = poll_msg.embeds[0]
    if poll_msg.author != ctx.message.guild.me:
      await ctx.send("That is not my poll.")
      return 
    if not mbed.to_dict()['footer']['text'].startswith('Author:'):
      await ctx.send("This is not my poll.")
      return
    options = [x.strip() for x in mbed.to_dict()['description'].split('\n')]
    op_dic = {x[:2] : x[:3] for x in options } if options[0][0] == '1'  else {x[:1] : x[2:] for x in options}
    voters = [ctx.message.guild.me.id]
    result = {x : 0 for x in op_dic.keys()}
    users = set()
    for reaction in poll_msg.reactions:
      if reaction.emoji in op_dic.keys():
        async for user in reaction.users():
          if user.id not in voters:
            voters.append(user.id)
            result[reaction.emoji]+=1
    output = d.Embed(title = "Results for {}".format(mbed.to_dict()['title']),description = '\n'.join(['{} : {}'.format(op_dic[key] , result[key]) for key in result.keys()]),color = 0xff9966)
    await ctx.send(embed = output)
   else:
    await ctx.send("You do not have the permissions to use this command.")

  start_time=time.time()
  @commands.command()
  async def uptime(self, ctx):
    current_time = time.time()
    difference = int(round(current_time - self.start_time))
    text = str(datetime.timedelta(seconds=difference))
    embed = discord.Embed(colour=0xc8dc6c)
    embed.set_thumbnail(url = str(self.bot.user.avatar_url))
    embed.add_field(name="Uptime", value=text)
    embed.set_footer(text=f"{self.bot.user.name}")
    try:
      await ctx.send(embed=embed)
    except discord.HTTPException:
      await ctx.send("Current uptime: " + text) 


def setup(client):
  client.add_cog(Useful_Commands(client))