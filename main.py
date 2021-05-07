import discord
from discord.ext import commands
import discord, datetime, time
import os
import asyncio
from discord.ext import tasks
import io
import games
import custom_commands
import info
import usefull_commands
import moderation
import music
intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='?', intents = intents)


@client.event
async def on_ready():
  activity = discord.Game(name = "annoying ZLD members", type = 3)
  await client.change_presence(status = discord.Status.idle, activity = activity)
  print('Hammy logged in as {0.user}'.format(client))

@client.event
async def on_member_join(member):
  channel=client.get_channel(778291814444040212)
  joined_member = int((time.time() - member.created_at.timestamp())//60//60//24)
  await channel.send(f"> **{member.name} account** has been created **{joined_member}** days ago.")
  

cogs = [custom_commands]

for i in range(len(cogs)):
  cogs[i].setup(client)

cogs = [games]

for i in range(len(cogs)):
  cogs[i].setup(client)

cogs = [info]

for i in range(len(cogs)):
  cogs[i].setup(client)

cogs = [usefull_commands]

for i in range(len(cogs)):
  cogs[i].setup(client)

cogs = [moderation]

for i in range(len(cogs)):
  cogs[i].setup(client)


cogs = [music]

for i in range(len(cogs)):
  cogs[i].setup(client)

client.run('ODA4MDE3MTAyMDQwNTk2NDkx.YCAakQ.afCA8itR1d1wpskDA0YWB2GQPDE')
