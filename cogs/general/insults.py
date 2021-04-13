from discord.ext import commands
from .. import custom_decorators
import discord
import random

class Insults(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    #@commands.check(custom_decorators.check_general)
    @commands.command(name = 'insult',
    brief = 'Will pick a random insult and use it',
    description = 'This function can take a name and use it in an insult.')
    async def random_insult(self, ctx, name: discord.Member):

        insult_dict = {
            'frankie': [
                "{} is like a cross between a tramp and a duckling"
            ]
        }

        response = random.choice(insult_dict['frankie'])
        await ctx.send("{}".format(response.format(name.name)))

def setup(bot):
    bot.add_cog(Insults(bot))