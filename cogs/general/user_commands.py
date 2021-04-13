from discord.ext import commands
from .. import custom_decorators
import discord
import random

class General(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.check(custom_decorators.check_general)
    @commands.command(name='nick',
    brief="Change your nickname",
    description="This command allows a user to change their nickname")
    async def change_nickname(self, ctx, nick):
        await ctx.author.edit(nick=nick)
        await ctx.send("Nickname change for {}".format(ctx.message.author.name))

    @commands.check(custom_decorators.check_general)
    @commands.command(name='8ball',
    brief="Magic 8ball will answer a question!",
    description='Ask the magic 8ball a question and receive an answer.\nUsage:')
    async def magic_8ball(self, ctx, question):

        answers = [
            'Check back later',
            'Unlikely...',
            'Get fucked noob',
            'Looks like rain',
            'This one time at bandcamp',
            'Time to die',
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes - Definitely',
            'You may rely on it',
            'As I see it, yes.',
            'Most likely',
            'Outlook good',
            'Yes.',
            'Signs point to yes',
            'Reply hazy, try again',
            'Ask again later.',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again.',
            'Don\'t count on it',
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
        ]
        response = random.choice(answers)
        await ctx.send(response)
    

    @commands.check(custom_decorators.check_general)
    @commands.command(name='roll',
    brief="Rolls a random number between 1 and 20",
    description="This command will select a random number between 1 and 20.\nUsage:")
    
    async def random_roll(self, ctx):

        if ctx.message.author.nick == None:
            await ctx.send("{} your number is {}".format(ctx.message.author.name, random.randint(1,21)))
        else:
            await ctx.send("{} your number is {}".format(ctx.message.author.nick, random.randint(1,21)))

def setup(bot):
    bot.add_cog(General(bot))