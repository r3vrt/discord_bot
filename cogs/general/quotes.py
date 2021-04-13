from discord.ext import commands
from .. import custom_decorators
import discord
import random

class Quotes(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.command(name='quote',
    brief="Quote a character. Deaults to Ron",
    description="This command allows a user to have a quote entered in channel")
    @commands.check(custom_decorators.check_general)
    async def quote_command(self, ctx, *args):
        
        quote_dict = {
            'Ron': [
            "There\'s only one thing I hate more than lying: skim milk. Which is water that is lying about being milk.",
            "I'd wish you the best of luck but I believe luck is a concept created by the weak to explain their failures.",
            "Dear frozen yogurt, you are the celery of desserts. Be ice cream or be nothing. Zero stars.",
            '''[Holds up iPod]\n\nTOM PUT ALL MY RECORDS INTO THIS RECTANGLE. THE SONGS JUST PLAY ONE AFTER THE OTHER. THIS IS AN EXCELLENT RECTANGLE.''',
            "Child labor laws are ruining this country",
            "I'm not interested in caring about people.",
            "Clear alcohols are for rich women on diets.",
            "Crying: Acceptable at funerals and the Grand Canyon.",
            "There are three acceptable haircuts: high and tight, crew cut, buzz cut.",
            '''The key to burning an ex-wife effigy is to dip it in paraffin wax and then toss the flaming bottle of isopropyl alcohol from a safe distance. 
            Do not stand too close when you light an ex-wife effigy.''',
            "There are only three ways to motivate people: money, fear, and hunger.",
            "Under my tutelage, you will grow from boys to men. From men into gladiators. And from gladiators into Swansons.",
            "Great job, everyone. The reception will be held in each of our individual houses, alone.",
            "On my deathbed, my final wish is to have my ex-wives rush to my side so I can use my dying breath to tell them both to go to hell one last time.",
            "Normally, if given the choice between doing something and nothing, I’d choose to do nothing. But I will do something if it helps someone else do nothing. I’d work all night, if it meant nothing got done.",
            "It's always a good idea to demonstrate to your coworkers that you are capable of withstanding a tremendous amount of pain.",
            "It’s pointless for a human to paint scenes of nature when they can go outside and stand in it.",
            "I call this turf ‘n’ turf. It’s a 16-ounce T-bone and a 24-ounce porterhouse. Also, whiskey and a cigar. I am going to consume all of this at the same time because I am a free American.",
            "I’m a simple man. I like pretty, dark-haired women, and breakfast food.",
            "So you talked to Tammy? What's it like to stare into the eye of Satan's butthole?",
            "No home is complete without a proper toolbox. Here’s April and Andy’s: A hammer, a half-eaten pretzel, a baseball card, some cartridge that says Sonic and Hedgehog, a scissor half, a flashlight filled with jellybeans.",
            "I once worked with a guy for three years and never learned his name. Best friend I ever had. We still never talk sometimes",
            "When people get too chummy with me I like to call them by the wrong name to let them know I don't really care about them.",
            "If any of you need anything at all, too bad. Deal with your problems yourselves, like adults.",
            "The government is a greedy piglet that suckles on a taxpayer’s teat until they have sore, chapped nipples.",
            "I don’t want to paint with a broad brush here, but every single contractor in the world is a miserable, incompetent thief.",
            "Fishing relaxes me. It’s like yoga, except I still get to kill something.",
            "Give a man a fish and feed him for a day. Don’t teach a man to fish…and feed yourself. He’s a grown man. And fishing’s not that hard.",
            "I like saying ‘No,’ it lowers their enthusiasm.",
        ],
        'Leslie': [
            "Random Quote"
        ]
        }
        if args:
            response = random.choice(quote_dict[str(args[0])])
            await ctx.send("{}:\n```{}```".format(str(args[0]), response) )
        else:
            response = random.choice(quote_dict['Ron'])
            await ctx.send("Ron:\n```{}```".format(response))



def setup(bot):
    bot.add_cog(Quotes(bot))