import discord
from discord.ext import commands
import json
import requests
import aiohttp 
from pyrandmeme import *


class API_Commands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    def get_quote(self):
     response = requests.get("https://zenquotes.io/api/random")
     json_data = json.loads(response.text)
     quote = '> ' + json_data[0]["q"] + "-" + '||' + json_data[0]["a"] + '||'
     return (quote)

    @commands.command(name = "inspire", description = "motivational quote")
    async def inspire(self,ctx):
     await ctx.send(self.get_quote())
    
    @commands.command(name = "dadjoke", aliases = ["dj", "dadjokes"], description = "tell you a dad joke")
    async def dadjoke(self,ctx):
        url = "https://dad-jokes.p.rapidapi.com/random/joke"
        headers ={'x-rapidapi-host': "dad-jokes.p.rapidapi.com",'x-rapidapi-key': "50a4f38679msh704c82e1d14329fp1e023ajsnaf7583db258b"}

        async with aiohttp.request('GET',url, headers= headers) as result:
            jokes = await result.json()
            await ctx.send(f"**{jokes['body'][0]['setup']}**\n\n**||{jokes['body'][0]['punchline']}||**")

        """
        async with ClientSession() as session:
            async with session.get(url, headers = headers) as response:
                r = await response.json()
                print(r)
                #await ctx.send(f"**{r['setup'][0]}**\n\n||{r['punchline'][0]}||")
        """

    @commands.command(name = "meme", description = "This command shows you a random meme.")
    async def _meme(self,ctx):
        await ctx.send(embed = await pyrandmeme())

def setup(client):
    client.add_cog(API_Commands(client))