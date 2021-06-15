import discord
import discord as d
import youtube_dl
from discord.ext import commands
import nacl
import DiscordUtils
import requests
import aiohttp
import json
import lyricsfinder
class Music(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  music = DiscordUtils.Music()

  @commands.command(name= "join",description = "Add the bot in the voice channel.",alias = "start")
  async def join(self,ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    if not voice:
     await ctx.send(f"I joined in {channel.mention}")
     await channel.connect()
    else:
      await ctx.send(f"{self.bot.user} is already connected to a voice channel.")
  
  @commands.command(name = "leave",aliases = ["dc","disconnect"],description = "Kick the bot from the voice channel.")
  async def leave(self, ctx):
    if ctx.voice_client:
     await ctx.voice_client.disconnect()
     await ctx.send("Successfully disconnected.")
    else:
      await ctx.send(f"{self.bot.user} is not in any voice channel.")
  
  @commands.command(name= "play", description = "Play a song.")
  async def play(self,ctx,*, url):
    voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)
    if not voice:
      await ctx.author.voice.channel.connect()
      await ctx.send(f"I joined in {ctx.author.voice.channel.mention}")
      
    player = self.music.get_player(guild=ctx.guild.id)
    if not player:
      player = self.music.create_player(ctx,ffmpeg_error_fix = True, ffmpeg_error_betterfix = True)
    if not ctx.voice_client.is_playing():
      await ctx.send("Searching...")
      await player.queue(url, search = True)
      song = await player.play()
      mbed = d.Embed(title = f"Playing {song.name} - {song.duration//60} min",color = 0xff9966)
      mbed.set_thumbnail(url = song.thumbnail)
      mbed.add_field(name = "Duration:", value = f"{song.duration//60} min", inline = True)
      await ctx.send(embed = mbed)
      await ctx.send(song.url)
    else:
      await ctx.send("Searching...")
      song = await player.queue(url, search = True)
      mbed = d.Embed(title = f"Queued {song.name}", color = 0xff9966)
      mbed.add_field(name = "Duration:", value = f"{song.duration//60} min", inline = False)
      mbed.add_field(name = "Queue index:", value = str(len(player.current_queue())-1),inline = False)
      mbed.set_thumbnail(url = song.thumbnail)
      await ctx.send(embed = mbed)
  
  @commands.command(name = "nowplaying", aliases = ["np"], description ="Shows what song the bot is currently playing.")
  async def _nowplaying(self,ctx):
    try:
     player = self.music.get_player(guild_id=ctx.guild.id)
     if not player.current_queue():
      await ctx.send("There is no song to show.")
     else:
      song = player.now_playing()
      await ctx.send(f"The current song is {song.name}")
    except AttributeError:
      await ctx.send(f"{self.bot.user} is not in any voice channel or there is no song in the player.")

  @commands.command(name = "pause", aliases = ["p"], description = "Pause the current song.")
  async def pause(self, ctx):
    try:
     player = self.music.get_player(guild_id=ctx.guild.id)
     if not player.current_queue():
      await ctx.send("There is no song to pause.")
     else:
      song = await player.pause()
      await ctx.send(f"Paused {song.name}")
    except AttributeError:
      await ctx.send(f"{self.bot.user} is not in any voice channel or there is no song in the player.")

  @commands.command(name ="resume", aliases = ["r"], description = "Resume the current song.")
  async def resume(self,ctx):
    try:
     player = self.music.get_player(guild_id=ctx.guild.id)
     if not player.current_queue():
       await ctx.send("There is no song to resume.")
     else:
      song = await player.resume()
      await ctx.send(f"Resumed {song.name}")
    except AttributeError:
      await ctx.send(f"{self.bot.user} is not in any voice channel or there is no song in the player.")
  
  @commands.command(name = "stop",aliases = ["sp"], description = "Stop the player.")
  async def stop(self, ctx):
    try:
     player = self.music.get_player(guild_id=ctx.guild.id)
     if not player.current_queue():
       await ctx.send("There is no song to stop.")
     else:
      song = await player.stop()
      await ctx.send(f"The player has been stopped.")
    except AttributeError:
      await ctx.send(f"{self.bot.user} is not in any voice channel or there is no song in the player.")
  
  @commands.command(name="loop",aliases = ["l"], description = "Loop the current song.")
  async def loop(self,ctx):
    try:
     player = self.music.get_player(guild_id=ctx.guild.id)
     if not player.current_queue():
       await ctx.send("There is no song to loop.")
     else:
      song = await player.toggle_song_loop()
      if song.is_looping:
       await ctx.send("Enabled loop for {}".format(song.name))
      else:
       await ctx.send("Disabled loop for {}".format(song.name))
    except AttributeError:
      await ctx.send(f"{self.bot.user} is not in any voice channel or there is no song in the player.")

  @commands.command(name = "queue",aliases = ["q"], description = "Shows the songs queue.")
  async def queue(self, ctx):
     try:
      player = self.music.get_player(guild_id=ctx.guild.id)
      number = 0
      mbed = d.Embed (title = "Song queue:", description = f"\n".join([str(player.current_queue().index(song)) + ". " + song.name + " - " + str(song.duration//60) + " min" for song in player.current_queue() ]),color = 0xff9966)
      mbed.set_thumbnail(url = ctx.guild.icon_url)
      await ctx.send(embed = mbed)
     except AttributeError:
       await ctx.send(f"{self.bot.user} is not in any voice channel or there is no song in the player.")

  @commands.command(name ="skip",aliases = ["s","next"], description = "Skip the current song.")
  async def skip(self,ctx):
    try:
     player = self.music.get_player(guild_id = ctx.guild.id)
     if not player.current_queue():
       await ctx.send("There is no song to skip.")
     else:
      data = await player.skip(force = True)
      await ctx.send(f"Skipped {data[0].name}")
    except AttributeError:
      await ctx.send(f"{self.bot.user} is not in any voice channel or there is no song in the player.")

  @commands.command(name= "volume",aliases = ["v"], description = "Changes the player volume")
  async def volume(self,ctx,number : int):
     try:
      player = self.music.get_player(guild_id = ctx.guild.id)
      if not player.current_queue():
       await ctx.send("There is no song to change volume for.")
      else:
       song, volume = await player.change_volume(int(number)/100)
       await ctx.send(f"Changed volume for {song.name} to {volume*100}%")
     except AttributeError:
      await ctx.send("The bot is not in any voice channel.")


  @commands.command(name = "remove", description = "Remove a song from the queue(index required).")
  async def remove(self, ctx, index :int):
     try:
      player = self.music.get_player(guild_id = ctx.guild.id)
      if not player.current_queue():
       await ctx.send("There is no song to remove.")
      else:
       song = await player.remove_from_queue(int(index))
       await ctx.send(f"Removed {song.name} from queue.")
     except AttributeError:
      await ctx.send("The bot is not in any voice channel or you typed an invalid index.")
  
  @commands.command(name = "save", aliases = ["savesong", "grab"], description = "Saves the current playing song to your DM.")
  async def _save(self,ctx):
    try:
      player = self.music.get_player(guild_id = ctx.guild.id)
      if not player.current_queue():
       await ctx.send("There is no song to save.")
      else:
        channel = await ctx.author.create_dm()
        song = player.now_playing()
        await channel.send(f"I saved this song for you: **{song.name}**")
        await ctx.send("Song saved.")
    except AttributeError: 
      await ctx.send("The bot is not in any voice channel.")


  """
  @commands.command(name = "lyrics", aliases = ["ly"], desription = "Shows the song lyrics.")
  async def lyrics(self, ctx,*, search ):
    lyrics = lyricsfinder.search_lyrics(search, google_api_key='AIzaSyCom4Ee9qAwtXuU4PsEx7ynrW3PkygRBAc')
    await ctx.send(lyrics.name)
    
    r = requests.get(f'https://api.lyrics.ovh/v1{search}')
    if r.status_code == 200:
      l_response =json.loads(r.content)
      print(l_response)
      try:
        
        lyric = l_response["lyrics"]
        await ctx.send(f"Here is the lyrics of this song: {lyric}")
      except:
        await ctx.send(f"Lyrics not found.")
    
    else:
      await ctx.send("Code errro")
    
  """

def setup(client):
  client.add_cog(Music(client)) 