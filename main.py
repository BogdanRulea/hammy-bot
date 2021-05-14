import discord
from discord.ext import commands
import discord, datetime, time
import os
import asyncio
from discord.ext import tasks
import json
import io

intents = discord.Intents.default()
intents.members = True

DEFAULTPREFIX = "?"

def get_prefix(client, message):
  with open("prefixes.json", "r") as f:
    data = json.load(f)
  
  if not str(message.guild.id) in data:
    return commands.when_mentioned_or("?")(client,message)
  return commands.when_mentioned_or(data[str(message.guild.id)])(client,message)
  
client = commands.Bot(command_prefix=DEFAULTPREFIX, intents = intents, help_command = None, owner_id = 241529498221281280)

@client.event
async def on_ready():
  activity = discord.Game(name = "with my wheel", type = 2)
  await client.change_presence(status = discord.Status.idle, activity = activity)
  print('Hammy logged in as {0.user}'.format(client))

"""
@client.event
async def on_message(message):
  if f"<@!{client.user.id}>" in message.content:
    
    with open("prefixes.json", "r") as f:
      data = json.load(f)
      
    if str(message.guild.id) in data:
      prefix = data[str(message.guild.id)]
    else:
      prefix = "?"

    await message.channel.send(f"My prefix is {prefix}. If you want to change the prefix use ``{prefix}prefix (prefix)``")

  
  await client.process_commands(message)
"""
@client.event
async def on_member_join(member):
  
  channel=client.get_channel(778291814444040212)
  guild = member.guild
  if discord.utils.get(guild.channels, name = channel.name):
   joined_member = int((time.time() - member.created_at.timestamp())//60//60//24)
   await channel.send(f"> **{member.name} account** was created **{joined_member}** days ago.\n**Reminder: For new members, make sure you assign them either the Pirate or Wizard Soapie role(s)!**")



client.load_extension('cogs.custom_commands')
client.load_extension('cogs.games')
client.load_extension('cogs.info')
client.load_extension('cogs.leveling')
client.load_extension('cogs.music')
client.load_extension('cogs.moderation')
client.load_extension('cogs.usefull_commands')
#client.load_extension('cogs.api')
client.run('ODA4MDE3MTAyMDQwNTk2NDkx.YCAakQ.afCA8itR1d1wpskDA0YWB2GQPDE')
