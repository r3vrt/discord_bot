import random
from .. import custom_decorators
from discord.ext import commands
import discord

def dice_roll(roller, sides, count):
       
    name = roller.nick if roller.nick else roller.name
    rangeCount = int(count[0]) if count else 1
    
    return "{} rolled: {}".format(name, [random.randint(1, sides) for _ in range(rangeCount)])


class DND_Tools(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d4",
    brief="Will roll a 4 sided dice",
    description="This command will output the result of a dice roll from 1 - 4. If you want multiple rolls add the number you want after the command.")
    async def dice_four(self, ctx, *args):

        await ctx.send(dice_roll(ctx.message.author, 4, args))

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d6",
    brief="Will roll a 6 sided dice",
    description="This command will output the result of a dice roll from 1 - 6. If you want multiple rolls add the number you want after the command.")
    async def dice_six(self, ctx, *args):

        await ctx.send(dice_roll(ctx, 6, args))

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d8",
    brief="Will roll an 8 sided dice",
    description="This command will output the result of a dice roll from 1 - 8. If you want multiple rolls add the number you want after the command.")
    async def dice_eight(self, ctx, *args):

        await ctx.send(dice_roll(ctx, 8, args))

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d10",
    brief="Will roll an 8 sided dice",
    description="This command will output the result of a dice roll from 1 - 8. If you want multiple rolls add the number you want after the command.")
    async def dice_ten(self, ctx, *args):

        await ctx.send(dice_roll(ctx, 10, args))

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d12",
    brief="Will roll a 12 sided dice",
    description="This command will output the result of a dice roll from 1 - 12. If you want multiple rolls add the number you want after the command.")
    async def dice_twelve(self, ctx, *args):

        await ctx.send(dice_roll(ctx, 12, args))

    @commands.check(custom_decorators.check_dnd)
    @commands.command(name="d20",
    brief="Will roll a 20 sided dice",
    description="This command will output the result of a dice roll from 1 - 20. If you want multiple rolls add the number you want after the command.")
    async def dice_twenty(self, ctx, *args):

        await ctx.send(dice_roll(ctx, 20, args))


def setup(bot):
    bot.add_cog(DND_Tools(bot))