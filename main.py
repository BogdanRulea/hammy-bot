import discord
from discord.ext import commands
import discord, datetime, time
import os
import asyncio
from discord.ext import tasks
#import json
import io
#import pymongo
#from pymongo import MongoClient




intents = discord.Intents.default()
intents.members = True

DEFAULTPREFIX = "?"

"""
cluster = MongoClient['mongodb+srv://hammybotdb:9aB0XQ0jbP8qp9sU@cluster0.g8mdi.mongodb.net/test']

DB = "BotData"

db = cluster[DB]

collection = db[DB]

def get_prefix(client, message):
  data = 

  if message.guild.id in data:
    return commands.when_mentioned_or(data[str(message.guild.id)])(client,message)
  if not str(message.guild.id) in data:
    return commands.when_mentioned_or("?")(client,message)
  
"""  
def new_func():
    return 241529498221281280

client = commands.Bot(command_prefix=DEFAULTPREFIX, intents = intents, help_command = None, owner_id = new_func(), case_insensitive = True)

@client.event
async def on_ready():
  Donations.start()
  activity = discord.Game(name = "with my wheel", type = 2)
  await client.change_presence(status = discord.Status.idle, activity = activity)
  print('Hammy logged in as {0.user}'.format(client))

"""
@client.event
async def on_message(message):
  if f"<@!{client.user.id}>" in message.content:
    
   

    if message.guild.id in data["Server_id"]:
      #my_prefix = data["Prefix"]
    else:
      mydic = {"Server_id" : str(message.guild.id), "Prefix" : DEFAULTPREFIX}
      my_prefix = DEFAULTPREFIX
      #collection.insert_one(mydic)

    await message.channel.send(my_prefix)

  await client.process_commands(message)
"""

@client.event
async def on_member_join(member):
  
  channel=client.get_channel(778291814444040212)
  guild = member.guild
  if discord.utils.get(guild.channels, name = channel.name):
   joined_member = int((time.time() - member.created_at.timestamp())//60//60//24)
   await channel.send(f"> **{member.name} account** was created **{joined_member}** days ago.\n**Reminder: For new members, make sure you assign them either the Pirate or Wizard Soapie role(s)!**")

@tasks.loop(hours = 12)
async def Donations():
  channel = client.get_channel(776345736392474634)
  await channel.send("Hi everyone I just wanted to say that I love you all and I hope you are ok.\nBe who you are and say what you feel, because those who mind don't matter, and those who matter don't mind.\nOh, one more thing before I go: If you like the bot and want to support it feel free to use the brand new `donate` command and help me buy a new wheel for hammy bot. <:hammylove:846810208202129409>")



client.load_extension('cogs.custom_commands')
client.load_extension('cogs.games')
client.load_extension('cogs.info')
client.load_extension('cogs.leveling')
client.load_extension('cogs.music')
client.load_extension('cogs.moderation')
client.load_extension('cogs.usefull_commands')
client.load_extension('cogs.api')
client.load_extension('cogs.donation')
client.run('ODA4MDE3MTAyMDQwNTk2NDkx.YCAakQ.afCA8itR1d1wpskDA0YWB2GQPDE')
