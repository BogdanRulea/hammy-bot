import discord
from discord.ext import commands
import json
import requests
from aiohttp import ClientSession



class API_commands(commands.Cog):
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
        headers ={'x-rapidapi-key': "50a4f38679msh704c82e1d14329fp1e023ajsnaf7583db258b", 'x-rapidapi-host': "dad-jokes.p.rapidapi.com"}
        async with ClientSession() as session:
            async with session.get(url, headers = headers) as response:
                r = await response.json()
                await ctx.send(f"**{r['setup']}**\n\n||{r['punchline']}||")

def setup(client):
    client.add_cog(API_commands(client))