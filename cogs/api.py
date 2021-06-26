import discord
from discord.ext import commands
import json
import requests
import aiohttp 
import discord as d
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
      
    
    @commands.command(name = "roast", description = "This command roast you or someone you mention.")
    async def _roast(self,ctx, member : discord.Member = None):
        if member == None:
            member = ctx.author
        
        url = "https://evilinsult.com/generate_insult.php?lang=en&type=json"
        response = requests.get(url)
        json_data = response.json()
        await ctx.send(f"**{member.name} - {json_data['insult']}**")
    
    @commands.command(name = "chucknorris", aliases = ["cn","legend","chuck","norris"], description = "Chuck Norris jokes.")
    async def _chuck(self,ctx):
        url = "https://api.chucknorris.io/jokes/random"
        response = requests.get(url)
        json_data = response.json()
        await ctx.send(f"**{json_data['value']}**")
    
    @commands.command(name = "urban", aliases = ["ud","dictionary","mean"], description = "Urban dictionary for discord.")
    async def _urban(self,ctx,*,term):
        
     url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

     querystring = {"term":term.lower()}

     headers = {'x-rapidapi-host': 'mashape-community-urban-dictionary.p.rapidapi.com','x-rapidapi-key': "50a4f38679msh704c82e1d14329fp1e023ajsnaf7583db258b"}

     response = requests.request("GET", url, headers=headers, params=querystring)

     json_data = response.json()

     mbed = d.Embed(title = f"Urban Dictionary for {term.lower()}:", color = 0xff9966)
     mbed.add_field(name = "Definition:", value = json_data["list"][0]["definition"],inline = False)
     await ctx.send(embed = mbed)
    
    """
    @commands.command(name = "country", description = "This command shows you the mentioned country info.")
    async def _country(self,ctx, country):
        url = "https://ip-geo-location.p.rapidapi.com/ip/check"

        querystring = {"format":"json","filter":"country","language":"en"}

        headers = {'x-rapidapi-host': 'ip-geo-location.p.rapidapi.com'}

        response = requests.request("GET", url, headers=headers, params=querystring)

        print(response.text)
    """
    
    @commands.command(name = "love", aliases = ["match"],description = "Love calculator.")
    async def _love(self,ctx, member  : discord.Member):
        url = "https://love-calculator.p.rapidapi.com/getPercentage"

        querystring = {"fname":ctx.author.name,"sname": member.name}

        headers = {'x-rapidapi-host': 'love-calculator.p.rapidapi.com','x-rapidapi-key': "50a4f38679msh704c82e1d14329fp1e023ajsnaf7583db258b"}
        response = requests.request("GET", url, headers=headers, params=querystring)

        json_data = response.json()

        mbed = d.Embed(title = "Love calculator", color = 0xff9966)

        mbed.add_field(name = "Lovers:" , value = f"{ctx.author.name} and {member.name}",inline = False)
        mbed.add_field(name = "Percentage:", value = json_data["percentage"], inline = True)
        mbed.add_field(name = "Result:", value = json_data["result"],inline = False)      

        await ctx.send(embed = mbed)
    
    """
    @commands.command(name = "country", description = "Country information.")
    async def _name(self,ctx,country):
        url = f"https://restcountries-v1.p.rapidapi.com/name/{country}"

        headers = {
         'x-rapidapi-key': "9a14a69cfcmsh31448a8a81dfd67p110f7djsn570e8d798fdd",
         'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
            }

        response = requests.request("GET", url, headers=headers)
        json_data = response.json()

        print(response.text)
        mbed = d.Embed(title = f"{country.upper()} info:",color = 0xff9966)
        mbed.add_field(name = "Name:", value = json_data[0]["name"],inline = False)
        mbed.add_field(name = "Calling Codes:", value = ", ".join(f for f in json_data[0]["callingCodes"]),inline = False)
        mbed.add_field(name = "Capital:", value = json_data[0]["capital"],inline = False)
        mbed.add_field(name = "Region:", value = json_data[0]["region"],inline = False)
        mbed.add_field(name = "SubRegion:", value = json_data[0]["subregion"],inline = False)
        mbed.add_field(name = "Population:", value = json_data[0]["population"],inline = False)
        mbed.add_field(name = "Timezones:", value = ", ".join(f for f in json_data[0]["timezones"]),inline = False)
        mbed.add_field(name = "Numeric Code:", value = json_data[0]["numericCode"],inline = False)
        mbed.add_field(name = "Currencies:", value = ", ".join(f for f in json_data[0]["currencies"]),inline = False)
        mbed.add_field(name = "Languages:", value = ", ".join(f for f in json_data[0]["languages"]),inline = False)
        mbed.add_field(name = "Borders:", value = ", ".join(f for f in json_data[0]["borders"]),inline = False)
        mbed.add_field(name = "Alt Spellings:", value = ", ".join(f for f in json_data[0]["altSpellings"]),inline = False)
        
        await ctx.send(embed = mbed)
    """
        
    """
    @commands.command(name = "news", description = "Latest news all around the world: Breaking news.")
    async def _news(self,ctx):

        url = "https://myallies-breaking-news-v1.p.rapidapi.com/GetTopNews"

        headers = {'x-rapidapi-host': 'myallies-breaking-news-v1.p.rapidapi.com'}

        response = requests.request("GET", url, headers=headers)

        print(response.text)
    """




def setup(client):
    client.add_cog(API_Commands(client))