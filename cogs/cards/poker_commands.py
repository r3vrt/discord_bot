import discord
from discord.ext import commands
from .. import custom_decorators

class Pokers(commands.Cog):

    def __init__(self, bot):

        self.bot = bot
    
    @commands.command(name='cards',
    brief="How many cards in a deck?",
    description="This command tells you how many cards in a deck.\nUsage:")
    @commands.check(custom_decorators.check_poker)
    async def cards(self, ctx):
        
        text = "52"
        response = text
        await ctx.send('There are {} cards in a  deck'.format(response))


    @commands.command(name='ranks',
    brief='Prints a list of hand ranks',
    description="This commanbd will print out a list of hand ranks in order.\nUsage:")
    @commands.check(custom_decorators.check_poker)
    async def poker_hand_ranks(self, ctx):
        response = '''
        The hand ranking in poker is as follows:
        A {dia} 5 {spa} 8 {dia} 9 {clu} 2 {hea}     : High Card
        A {dia} A {clu} 3 {hea} 6 {dia} 7 {dia}     : Pair
        A {dia} A {clu} K {hea} K {dia} 3 {clu}     : Two Pair
        A {dia} A {clu} A {hea} K {clu} 7 {dia}     : Three of a Kind
        A {dia} K {hea} Q {clu} J {dia} 10 {dia}    : Straight
        A {dia} 5 {dia} 8 {dia} 9 {dia} 3 {dia}      : Flush
        A {dia} A {hea} A {clu} K {dia} K {hea}     : Full House
        A {dia} A {hea} A {clu} A {spa} K {dia}     : Four of a Kind
        5 {dia} 6 {dia} 7 {dia} 8 {dia} 9 {dia}       : Straight Flush
        A {hea} K {hea} Q {hea} J {hea} 10 {hea}    : Royal Flush
        '''.format(dia=":diamonds:", hea=":hearts:", clu=":clubs:", spa=":spades:")

        await ctx.send(response)


def setup(bot):
    bot.add_cog(Pokers(bot))