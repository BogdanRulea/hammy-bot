import discord
from discord.ext import commands
import io
import os
import discord, datetime, time 
import discord as d
class Moderation(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  @commands.command()
  async def hmyeat(self,ctx, *, number:int=None):
   if ctx.message.author.guild_permissions.manage_messages :
    try:
      if number == None:
        await ctx.channel.send("You must input a number.")
      else:
        deleted = await ctx.message.channel.purge(limit = number + 1)
        await ctx.channel.send(f"Messages purged by {ctx.message.author}: `{len(deleted)-1}`")
    except:
      await ctx.channel.send("I can't purge messages here.")
   else:
    await ctx.channel.send("You don't have the permissions to use this command.")

  @commands.command()
  async def userinfo(self,ctx, member : discord.Member = None):
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
  
  @commands.command()
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

  @commands.command()
  async def witness(self,ctx, member : discord.Member):
   if ctx.author.guild_permissions.manage_permissions:
    perms = ctx.channel.overwrites_for(member)
    await ctx.channel.set_permissions(member, read_messages = not perms.read_messages, send_messages = not perms.send_messages, attach_files = not perms.attach_files, embed_links = not perms.embed_links, read_message_history = not perms.read_message_history, send_tts_messages = not perms.send_tts_messages, add_reactions = not perms.add_reactions)
    await ctx.channel.send(f"{member.name}'s permissions have been toggled")
   else:
    await ctx.send("**You don't have the permissions to use this command.**")

  @commands.command()
  async def case_closed(self,ctx, channel : d.TextChannel):
   if ctx.author.guild_permissions.manage_messages:
    await ctx.message.channel.purge(limit = 1)
    mbed = d.Embed(title = 'Success', description = f'Channel: {channel} has been closed',colour=discord.Colour(0xff9966))
    await ctx.send(embed = mbed)

    filename = f"{channel.name}.txt"
    with open(filename, "w") as file:
      async for msg in channel.history(limit=None):
        file.write(f"{msg.created_at} - {msg.author.display_name}: {msg.clean_content}\n")
    with open(filename, "rb") as file:
      await ctx.send(f"**The {channel.name} transcript is: **", file = discord.File(file,f"{filename}"))
    
    await channel.delete()
   else:
    await ctx.send('**You do not have the permissions to delete this channel.**')

  @commands.command()
  async def serverinfo(ctx):
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
   mbed.add_field(name = 'Creation Date:', value = ctx.guild.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'),inline = False)
   mbed.add_field(name = 'Server ID:', value = id_guild, inline = True)
   mbed.add_field(name = 'Region:', value = region, inline = True)
   mbed.add_field(name = 'Channels:', value = channels, inline = False)
   mbed.add_field(name = 'Number of roles:', value = roles, inline = True)
   mbed.add_field(name = 'Number of members:', value = memberCount, inline = True)
   mbed.add_field(name = "Bots:", value = (','.join(list_of_bots)), inline = False)
   mbed.add_field(name = 'Verification Level:', value = str(ctx.guild.verification_level), inline = True)
   await ctx.send(embed = mbed)


def setup(client):
  client.add_cog(Moderation(client))