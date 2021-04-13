import discord
import sys
import traceback

from discord.ext import commands

class commandErrors(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.errors.CheckFailure):

            await ctx.send("```Incorrect command. Please check the help: \n{}help```".format(ctx.prefix))

            pass

        if isinstance(error, commands.errors.MissingRequiredArgument):

            await ctx.send("```Incorrect Usage. Please check the help.\n{}help {}```".format(ctx.prefix, ctx.command.name))

            pass

        else:
            print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
            traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(bot):
    bot.add_cog(commandErrors(bot))