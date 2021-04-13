from discord.ext import commands
import discord
from yahoo_fin import stock_info as si

class Finance(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

   
    @commands.command(name="stonks",
    brief="Displays current price of stock",
    description="this command will show the user the current price of the stock ticker")
    async def stonks(self, ctx, ticker):
        await ctx.send("The current price of {} is {}".format(ticker, round(float(si.get_live_price(ticker)), 2)))


    @commands.command(name='crypto',
    brief='This will list the top 100 cryptos prices',
    description='This command lists out the top 100 cryptos prices by default.')
    async def crypto(self, ctx):
        await ctx.send(si.get_top_crypto())
        

def setup(bot):
    bot.add_cog(Finance(bot))