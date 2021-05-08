import discord
import discord as d
import youtube_dl
from discord.ext import commands
import nacl
import DiscordUtils
class Music(commands.Cog):
  def __init__(self,bot):
    self.bot=bot

  music = DiscordUtils.Music()

  @commands.command(name= "join",description = "add the bot in the voice channel",alias = "start")
  async def join(self,ctx):
    channel = ctx.author.voice.channel
    voice = discord.utils.get(self.bot.voice_clients, guild=ctx.guild)
    if not voice:
     await channel.connect()
    else:
      await ctx.send(f"{self.bot.user} is already connected to a voice channel.")
  
  @commands.command(name = "leave",aliases = ["dc","disconnect"],description = "kick the bot from the voice channel")
  async def leave(self, ctx):
    if ctx.voice_client:
     await ctx.voice_client.disconnect()
    
    else:
      await ctx.send(f"{self.bot.user} is not in any voice channel.")
  
  @commands.command(name= "play", description = "play a song")
  async def play(self,ctx,*, url):
    voice = discord.utils.get(self.bot.voice_clients, guild = ctx.guild)
    if not voice:
      await ctx.author.voice.channel.connect()
    player = self.music.get_player(guild=ctx.guild.id)
    if not player:
      player = self.music.create_player(ctx, ffmpeg_error_betterfix = True)
    if not ctx.voice_client.is_playing():
      await player.queue(url, search = True)
      song = await player.play()
      await ctx.send(f"Playing {song.name}.")
    else:
      song = await player.queue(url, search = True)
      await ctx.send(f"Queued {song.name}.")
  
  @commands.command(name = "pause", aliases = ["p"], description = "pause the current song")
  async def pause(self, ctx):
    player = self.music.get_player(guild_id=ctx.guild.id)
    song = await player.pause()
    await ctx.send(f"Paused {song.name}")

  @commands.command(name ="resume", aliases = ["r"], description = "resume the current song")
  async def resume(self,ctx):
    player = self.music.get_player(guild_id=ctx.guild.id)
    song = await player.resume()
    await ctx.send(f"Resumed {song.name}")
  
  @commands.command(name = "stop",aliases = ["sp"], description = "stop the player")
  async def stop(self, ctx):
    player = self.music.get_player(guild_id=ctx.guild.id)
    song = await player.stop()
    await ctx.send(f"The player has been stopped.")
  
  @commands.command(name="loop",aliases = ["l"], description = "loop the current song")
  async def loop(self,ctx):
    player = self.music.get_player(guild_id=ctx.guild.id)
    song = await player.toggle_song_loop()
    if song.is_looping:
      await ctx.send("Enabled loop for {}".format(song.name))
    else:
      await ctx.send("Disabled loop for {}".format(song.name))

  @commands.command(name = "queue",aliases = ["q"], description = "shows the songs queue")
  async def queue(self, ctx):
    player = self.music.get_player(guild_id=ctx.guild.id)
    number = 0
    mbed = d.Embed (title = "Song queue:", description = f"\n- ".join([song.name for song in player.current_queue()]),color = 0xff9966)
    mbed.set_thumbnail(url = ctx.guild.icon_url)
    await ctx.send(embed = mbed)

  @commands.command(name ="skip",aliases = ["s"], description = "skip the current song")
  async def skip(self,ctx):
    player = self.music.get_player(guild_id = ctx.guild.id)
    data = await player.skip(force = True)
    await ctx.send(f"Skipped {data[0].name}")

  @commands.command(name= "volume",aliases = ["v"], description = "changes the player volume")
  async def volume(self,ctx, number : float):
    try:
      player = self.music.get_player(guild_id = ctx.guild.id)
      song, volume = await player.change_volume(float(number)/100)
      await ctx.send(f"Changed colume for {song.name} to {volume*100}%")
    except AttributeError:
      await ctx.send("You have to type a valid float number between 0 and 1.")

  @commands.command(name = "remove", description = "remove a song from the queue(index required)")
  async def remove(self, ctx, index :int):
    try:
     player = self.music.get_player(guild_id = ctx.guild.id)
     song = await player.remove_from_queue(int(index))
     await ctx.send(f"Removed {song.name} from queue.")
    except AttributeError:
      await ctx.send("You have to type a valid number.")

def setup(client):
  client.add_cog(Music(client)) 