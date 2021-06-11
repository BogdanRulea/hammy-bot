import discord
from discord.ext import commands
import discord as d
from discord import DMChannel
class Donations(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = "donate", description = "If you like the bot and wanna support it feel free to donate any amount of money you'd like.Ty for support!!!")
    async def donate(self,ctx):
        author = ctx.author

        channel = await author.create_dm()

        mbed = d.Embed(title = "Donator is the best hamster", description = "Thank you for using the bot and i hope you like it.\nIf you want to support my work and wanna help hammy bot get a new wheel feel free to donate any amount of money you'd like.\n More updates and a lot of cool stuffs coming soon.", color = 0xff9966)
        
        user = await self.bot.fetch_user("241529498221281280")
        
        await DMChannel.send(user,f"{author.name} - ({author.id}) used the `donate` command in {ctx.guild.name}")

        #await self.bot.send_message(me,)

        await channel.send(embed = mbed)
        await channel.send("**Here is the donation link(PayPal):** https://www.paypal.me/transactionspayment")


def setup(client):
    client.add_cog(Donations(client))