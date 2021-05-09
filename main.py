import discord
from discord.ext import commands
import discord, datetime, time
import os
import asyncio
from discord.ext import tasks
import io
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='?', intents = intents, help_command = None, owner_id = 241529498221281280)


@client.event
async def on_ready():
  activity = discord.Game(name = "annoying ZLD members", type = 3)
  await client.change_presence(status = discord.Status.idle, activity = activity)
  print('Hammy logged in as {0.user}'.format(client))

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

client.run('ODA4MDE3MTAyMDQwNTk2NDkx.YCAakQ.afCA8itR1d1wpskDA0YWB2GQPDE')
