import random
from .. import custom_decorators
from discord.ext import commands
import discord

class DND_Tools(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d4",
    brief="Will roll a 4 sided dice",
    description="This command will output the result of a dice roll from 1 - 4. If you want multiple rolls add the number you want after the command.")
    async def dice_four(self, ctx, *args):

        if ctx.message.author.nick:
            name = ctx.message.author.nick
        else:
            name = ctx.message.author.name

        if args:
            result =  [random.randint(1, 4) for _ in range(int(args[0]))]
            await ctx.send("You rolled: {}".format(result))
        else:
            await ctx.send("{} rolled: {}".format(name, random.randint(1, 4)))
        

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d6",
    brief="Will roll a 6 sided dice",
    description="This command will output the result of a dice roll from 1 - 6. If you want multiple rolls add the number you want after the command.")
    async def dice_six(self, ctx, *args):

        if ctx.message.author.nick:
            name = ctx.message.author.nick
        else:
            name = ctx.message.author.name

        if args:
            result =  [random.randint(1, 6) for _ in range(int(args[0]))]
            await ctx.send("You rolled: {}".format(result))
        else:
            await ctx.send("{} rolled: {}".format(name, random.randint(1, 6)))

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d8",
    brief="Will roll an 8 sided dice",
    description="This command will output the result of a dice roll from 1 - 8. If you want multiple rolls add the number you want after the command.")
    async def dice_eight(self, ctx, *args):

        if ctx.message.author.nick:
            name = ctx.message.author.nick
        else:
            name = ctx.message.author.name

        if args:
            result =  [random.randint(1, 8) for _ in range(int(args[0]))]
            await ctx.send("You rolled: {}".format(result))
        else:
            await ctx.send("{} rolled: {}".format(name, random.randint(1, 8)))


    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d12",
    brief="Will roll a 12 sided dice",
    description="This command will output the result of a dice roll from 1 - 12. If you want multiple rolls add the number you want after the command.")
    async def dice_twelve(self, ctx, *args):

        if ctx.message.author.nick:
            name = ctx.message.author.nick
        else:
            name = ctx.message.author.name

        if args:
            result =  [random.randint(1, 12) for _ in range(int(args[0]))]
            await ctx.send("You rolled: {}".format(result))
        else:
            await ctx.send("{} rolled: {}".format(name, random.randint(1, 12)))

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d20",
    brief="Will roll a 20 sided dice",
    description="This command will output the result of a dice roll from 1 - 20. If you want multiple rolls add the number you want after the command.")
    async def dice_twenty(self, ctx, *args):

        if ctx.message.author.nick:
            name = ctx.message.author.nick
        else:
            name = ctx.message.author.name

        if args:
            result =  [random.randint(1, 20) for _ in range(int(args[0]))]
            await ctx.send("You rolled: {}".format(result))
        else:
            await ctx.send("{} rolled: {}".format(name, random.randint(1, 20)))

            
def setup(bot):
    bot.add_cog(DND_Tools(bot))