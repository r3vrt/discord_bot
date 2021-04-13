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
    async def random_insult(self, ctx, name: discord.Member, *args):

        insult_dict = {
            'frankie': [
                "{} is like a cross between a tramp and a duckling",
                "{} looks like someone put a sheep's teeth into a baby's head",
                "Nobody in Britain wants {} to be deported. We'd much rather they were strangled in their bed by Santa"
            ],
            'random': [
                "{}, you’re the reason God created the middle finger.",
                "{} is a gray sprinkle on a rainbow cupcake.",
                "{}, you bring everyone so much joy! You know, when you leave the room. But, still.",
                "{}, I hope your spouse brings a date to your funeral.",
                "{}, mirrors can't talk. Lucky for you, they cant laugh either."


            ]
        }

        if args:
            response = random.choice(insult_dict[str(args[0])])
            await ctx.send(response.format(name.name))
        else:
            dic_key = random.choice(list(insult_dict.keys()))
            response = random.choice(insult_dict[dic_key])
            await ctx.send("{}".format(response.format(name.name)))

def setup(bot):
    bot.add_cog(Insults(bot))