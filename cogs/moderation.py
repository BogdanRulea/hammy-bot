import discord
from discord import webhook
from discord.ext import commands
import io
import os
import sys
import discord, datetime, time 
import asyncio
import discord as d
import chat_exporter
from discord.ext.commands.cog import Cog
from discord.ext.commands.errors import MemberNotFound, RoleNotFound
from discord_webhook import DiscordWebhook, DiscordEmbed
class Moderation(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command(name = "hmyeat", aliases = ["hclear","hpurge"], description = "purge the given number of messages from the channel (Command for middleman, mod+)")
  async def hmyeat(self,ctx, *, number:int=None):
   if ctx.message.author.guild_permissions.manage_messages:
    try:
      if number == None:
        await ctx.channel.send("You must input a number.")
      else:
        deleted = await ctx.message.channel.purge(limit = number + 1)
        channels  = ctx.guild.get_channel(776678190831632414)
        await channels.send(f"{ctx.author.name} has purged {len(deleted)-1} messages in {ctx.channel.mention}.")
        await ctx.message.channel.purge(limit = 1)
    except AttributeError:
      await ctx.channel.send("Purge error.")
   else:
    await ctx.channel.send("You don't have the permissions to use this command.")

  @commands.command(name= "userinfo",aliases = ["profile"] ,description = "shows user's info")
  async def userinfo(self,ctx, member : discord.Member = None):
   try:
     if member == None:
      member = ctx.author
   
     date_format = "%a, %d %b %Y %I:%M %p"
     mbed = d.Embed(color = 0xff9966, description = f"{member.mention}")
     mbed.set_author(name = str(member), icon_url = member.avatar_url)
     mbed.set_thumbnail(url = str(member.avatar_url))
     mbed.add_field(name = "Joined:", value = f"{member.joined_at.strftime(date_format)}\n({int((time.time()-member.joined_at.timestamp())//60//60//24)} days ago)")
     members = sorted(ctx.guild.members, key = lambda m : m.joined_at)
     mbed.add_field(name = "Join position:", value = str(members.index(member)+1))
     mbed.add_field(name = "Registered:", value = f"{member.created_at.strftime(date_format)}\n({int((time.time() - member.created_at.timestamp())//60//60//24)} days ago)")

     if len(member.roles)>1:
      role_find=','.join([r.mention for r in member.roles][1:])
      if len(member.roles)<20:
       mbed.add_field(name = "Roles [{}]".format(len(member.roles) -1), value = role_find, inline = False)
      else:
       mbed.add_field(name = "Roles [{}]".format(len(member.roles) -1), value = "Too many roles to show.", inline = False)
     highest_role = member.roles
     highest_role.reverse()
     mbed.add_field(name = "Highest Role:", value = highest_role[0], inline = False)
     perm_find = ', '.join(str(p[0]).replace('_',' ') for p in member.guild_permissions if p[1])
     mbed.add_field(name = "Guild permissions:", value = perm_find, inline = False)
     mbed.timestamp = datetime.datetime.utcnow()
     mbed.set_footer(text = f"ID: {str(member.id)}/")
     await ctx.send(embed = mbed)
   except MemberNotFound:
     await ctx.send(f"Member not found")
    
   """
    date_format = "%a, %d %b %Y %I:%M %p"
    mbed = d.Embed(color = 0xff9966, description = f"{member.mention}")
    mbed.set_author(name = str(member), icon_url = member.avatar_url)
    mbed.set_thumbnail(url = str(member.avatar_url))
    mbed.add_field(name = "Registered:", value = f"{member.created_at.strftime(date_format)}\n({int((time.time() - member.created_at.timestamp())//60//60//24)} days ago)")
    mbed.timestamp = datetime.datetime.utcnow()
    mbed.set_footer(text = f"ID: {str(member.id)}/")
    await ctx.send(embed = mbed)
   """
  """
  @commands.command()
  async def catcreate(self,ctx, role : discord.Role, *, name):
   
   overwrites = {
     ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, manage_channels=False, manage_permissions = False),
     ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
     role: discord.PermissionOverwrite(read_messages=True, manage_channels= True, manage_permissions = True)
   }
   category = await ctx.guild.create_category(name = name, overwrites=overwrites)
   mbed = d.Embed(title = "Success", description = f"{category.name} category has been created. ",colour=discord.Colour(0xff9966))
   await ctx.send(embed = mbed)
  """
  @commands.command(name = "case_open", description = "create a channel for member's case", hidden = True)
  async def case_open(self,ctx, judge : discord.Member, *, member : discord.Member):
   if ctx.author.guild_permissions.manage_channels:
    overwrites = {
    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, manage_channels= False, manage_permissions = False,create_instant_invite=False, send_messages = False, attach_files = False, embed_links = False, add_reactions=False, mention_everyone = False, use_external_emojis = False, read_message_history= False, manage_webhooks = False, manage_messages = False, send_tts_messages = False),
    
    ctx.guild.me: discord.PermissionOverwrite(read_messages=True, manage_channels= True, manage_permissions = True, send_messages = True, attach_files = True, embed_links = True, add_reactions=True, use_external_emojis = True, read_message_history= True, manage_webhooks = True, manage_messages = True, send_tts_messages = True),
    
    member: discord.PermissionOverwrite(read_messages=True, manage_channels= False, manage_permissions = False,create_instant_invite=False, send_messages = True, attach_files = True, embed_links = True, add_reactions=True, mention_everyone = False, use_external_emojis = True, read_message_history= True, manage_webhooks = False, manage_messages = False, send_tts_messages = True),
   
    judge: discord.PermissionOverwrite(read_messages=True, manage_channels= True, manage_permissions = True, send_messages = True, attach_files = True, embed_links = True, add_reactions=True, use_external_emojis = True, read_message_history= True, manage_webhooks = True, manage_messages = True, send_tts_messages = True)
    }

    channel = await ctx.guild.create_text_channel(name = f'{member.name} case', overwrites=overwrites, category = self.bot.get_channel(828331400942845972))
    mbed = d.Embed(title = "Success", description = f"{channel.mention} channel has been created. ",colour=discord.Colour(0xff9966))
    await ctx.send(embed = mbed)
   else:
    await ctx.send("**You don't have the permissions to use this command**")

  @commands.command(name = "witness", aliases = ["add","toggle"], description = "add/kick witnesses from interrogation channels", hidden = True)
  async def witness(self,ctx, member : discord.Member):
   if ctx.author.guild_permissions.manage_permissions:
    perms = ctx.channel.overwrites_for(member)
    await ctx.channel.set_permissions(member, read_messages = not perms.read_messages, send_messages = not perms.send_messages, attach_files = not perms.attach_files, embed_links = not perms.embed_links, read_message_history = not perms.read_message_history, send_tts_messages = not perms.send_tts_messages, add_reactions = not perms.add_reactions)
    await ctx.channel.send(f"{member.name}'s permissions have been toggled")
   else:
    await ctx.send("**You don't have the permissions to use this command.**")

  @commands.command(name = "case_closed", description = "delete the specified channel and send the transcript in the channel where the command was appealed", hidden = True)
  async def case_closed(self,ctx, channel : d.TextChannel):
   if ctx.author.guild_permissions.manage_channels:
    await ctx.message.channel.purge(limit = 1)
    mbed = d.Embed(title = 'Success', description = f'Channel: {channel} has been closed',colour=discord.Colour(0xff9966))
    await ctx.send(embed = mbed)

    transcript = await chat_exporter.export(channel)
    if transcript is None:
      await ctx.send("This channel has no messages")
      return
    
    transcript_file = discord.File(io.BytesIO(transcript.encode()), filename = "transcript-{}.html".format(channel.name))
    await channel.delete()
    await ctx.send(file=transcript_file)
   else:
    await ctx.send('**You do not have the permissions to delete this channel.**')

  @commands.command(name = "serverinfo", description = "shows server information")
  async def serverinfo(self,ctx):
   name = str(ctx.guild.name)
   description = str(ctx.guild.description)
   owner = str(ctx.guild.owner)
   id_guild = str(ctx.guild.id)
   region =str(ctx.guild.region)
   memberCount = str(ctx.guild.member_count)
   icon = str(ctx.guild.icon_url)
   roles = str(len(ctx.guild.roles))
   channels = str(len(ctx.guild.channels))
   list_of_bots = [bot.mention for bot in ctx.guild.members if bot.bot]
   mbed = d.Embed(title = name + ' Server Info:', description = 'Description: '+ description, color = 0xff9966)
   mbed.set_thumbnail(url=icon)
   mbed.add_field(name = 'Owner:', value = owner, inline = False)
   mbed.add_field(name = 'Creation Date:', value = f"{ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')}\n({int((time.time()-ctx.guild.created_at.timestamp())//60//60//24)} days ago)",inline = False)
   mbed.add_field(name = 'Server ID:', value = id_guild, inline = True)
   mbed.add_field(name = 'Region:', value = region, inline = True)
   mbed.add_field(name = 'Channels:', value = channels, inline = False)
   mbed.add_field(name = 'Number of roles:', value = roles, inline = True)
   mbed.add_field(name = 'Number of members:', value = memberCount, inline = True)
   mbed.add_field(name = "Bots:", value = (','.join(list_of_bots)), inline = False)
   mbed.add_field(name = 'Verification Level:', value = str(ctx.guild.verification_level), inline = True)
   mbed.set_author(name = str(ctx.author.name),url=ctx.author.avatar_url)
   mbed.timestamp=datetime.datetime.utcnow()

   await ctx.send(embed = mbed)
  
  @commands.command(name = "serverupdate", aliases = ["su","serverupdates","updates"],description = "This command post an announcement in server updates section using a webhook.")
  async def _serverupdate(self,ctx):
    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel

    await ctx.send("Ok, you can write the update description below.")

    message = await self.bot.wait_for("message", check = check)

    webhook = DiscordWebhook(url = 'https://discord.com/api/webhooks/780594092602163200/T65Xl-QN6cgkcn0lItJ9ulxDhw24vn0u4CY6sUaQIra8w9zvop3S3_pn-NTXxtYo2Dky')

    mbed = DiscordEmbed(title = "Server Update", description = str(message.content), color = '00ffe3')

    webhook.add_embed(mbed)
    webhook_post = webhook.execute()

    embed = d.Embed(title = "Success", description = f"The announcement was successfully posted.",colour=discord.Colour(0xff9966))
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    await ctx.send(embed = embed)

  """
  @commands.command(name = "ban", aliases = ["yeet"], description = "Ban the mentioned server member.")
  @commands.has_guild_permissions(administrator = True)
  async def _ban(self,ctx,member : discord.Member,*, reason = None):
  """
  @commands.command(name = "check_role", aliases = ["srole"], description = "Check if the role exist in the server.")
  @commands.has_guild_permissions(manage_roles = True)
  async def _role1(self,ctx, role:discord.Role):
    try:
     if discord.utils.get(ctx.guild.roles,name = role.name):
      await ctx.send(f"The {role.name} role already exist in the server.")
    except RoleNotFound:
      await ctx.send("The role is not in the server.")

  @commands.command(name = "create_role", aliases = ["crole"], description = "Create a custom role.")
  @commands.has_guild_permissions(administrator = True)
  async def _role2(self,ctx):
    
    def check(msg):
      return msg.author == ctx.author and msg.channel == ctx.channel
    
    try:
     await ctx.send("Now type the role name.")
     response = await self.bot.wait_for("message", check = check)

     await ctx.send("Now type the color you would like the role to be.")
     color = await self.bot.wait_for("message", check = check)
     color_value = int(hex(int(color.content.replace('#',''),16)),0)
     await ctx.guild.create_role(name = response.content, colour = color_value)
     await ctx.send(f"{response.content} role has been created.\n**You can check it in the server roles list.**")
    except ValueError:
      await ctx.send("You have to type a valid color code.")
  
  @commands.command(name = "delete_role", aliases = ['delrole', 'drole'], description = "Delete a server role.")
  @commands.has_guild_permissions(administrator = True)
  async def _role3(self, ctx, role : discord.Role):
    try:
     role = discord.utils.get(ctx.guild.roles,name = role.name)
     if role:
      await role.delete()
      await ctx.send(f"The {role.name} role has been deleted!")
    except RoleNotFound:
      await ctx.send("The role is not in the server.")

  """
  @commands.command(name = "kick", aliases = ["yeet"], description = "Kick a member from the server.")
  @commands.has_guild_permissions(kick_members = True)
  async def _kick(self, ctx, member : discord.member,*,reason = None):
    await self.bot.kick()
    mbed = d.Embed(title = "Warning!!!", description = f"You have been kicked from {ctx.guild.name} for the following reason: {reason}.", color = 0xff9966)
  """  
  @commands.command(name = "reload", descripition = "Reload a module.")
  @commands.has_guild_permissions(administrator = True)
  async def _reload(self,ctx, name):
    self.bot.unload_extension("cogs."+name)
    self.bot.load_extension("cogs."+name)
    await ctx.send(f"{name} module has been reloaded.")

  """
  @commands.command(name ="afk", description = "This command make you AFK")
  async def afk(self,ctx,time ,*,reason = "No reason given"):
    current_nickname = ctx.author.nick
    
    seconds = 0

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
    elif seconds > 7776000:
     ctx.send("You can't set the timer for more than 90 days.")
     return
    else:
      ctx.send("Time invalid please try again!")
      return
    await ctx.send(f"{ctx.author.mention} is afk for {counter}: {reason}")
    await ctx.author.edit(nick = f"[AFK]{ctx.author.name}")
    await asyncio.sleep(seconds)
    await ctx.author.edit(nick = current_nickname)
    await ctx.send(f"{ctx.author.mention} is no longer AFK")
    """



  




def setup(client):
  client.add_cog(Moderation(client))