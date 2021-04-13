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
                "{}, mirrors can't talk. Lucky for you, they cant laugh either.",
                "{}, Did your parents have any children that lived?",
                "{}, Does your ass ever get jealous of the shit that comes out of your mouth?",
                "Don’t make me have to smack the extra chromosome out of you {}.",
                "Everyone that has ever said they love you was wrong {}.",
                "{}, For years your mother and I wanted kids. Imagine our disappointment when you came along.",
                "How did you crawl out of the abortion bucket, {}?",
                "How do you even masturbate knowing whose dick you’re touching {}?",
                "How the fuck are you the sperm that won {}?",
                "{}, I bet you swim with a T-shirt on.",
                "I can explain it to you {}, but I can’t understand it for you.",
                "I could agree with you {}, but then we’d both be wrong.",
                "{}, I don’t have the time or the crayons to explain this to you.",
                "I envy people who have never met you, {}.",
                "{}, I hope you have beautiful children and that they all get cancer.",
                "I want {} to be the pallbearer at my funeral so they can let me down one last time.",
                "I’d call you a cunt {}, but you have neither the warmth or the depth.",
                "Hey {}, I’d love to stay and chat but I’d rather have type-2 diabetes.",
                "I’d offer {} a shit sandwich, but I hear they don’t like bread.",
                "I’ll plant a mango tree in {}'s mother’s cunt and fuck their sister in its shade.",
                "{}, I’m sorry your dad beat you instead of cancer.",
                "I’ve forgotten more than you know, {}.",
                "If genius skips a generation, your children will be brilliant {}.",
                "If I wanted any shit out of {} I’d take my dick out of their ass.",
                "If I wanted to commit suicide I’d climb to {}'s ego and jump to their IQ.",
                "If my dog had a face like {}, I’d paint his ass and teach him to walk backwards.",
                "If the road were paved with dicks, {}'s mother would walk on her ass.",
                "If there was a single intelligent thought in {}'s head it would have died from loneliness.",
                "If {} could suck their own dick then they would finally suck at everything.",
                "If {} was a potato they’d be a stupid potato.",
                "If {} was an inanimate object, they’d be a participation trophy.",
                "If {} was any dumber, someone would have to water them twice a week.",
                "If {} was on fire and I had a cup of my own piss, I’d drink it.",
                "If {} was twice as smart, they’d still be stupid.",
                "If {}'s parents were to divorce, would they still be brother and sister?",
                "In a country where anyone can be anything, I will never understand why {} chose to be mediocre.",
                "May {}'s balls turn square and fester at the corners.",
                "Maybe if {} eats all that makeup they will be beautiful on the inside.",
                "No offense, but {} makes me want to staple my cunt shut.",
                "People like {} are the reason God doesn’t talk to us anymore.",
                "People will not only remember {}'s death, they will celebrate it.",
                "Ready to fail like {}'s dad’s condom?",
                "{}, shut your mouth, I can smell your Dad’s cock.",
                "{}, anyone who would fuck you ain’t worth fucking.",
                "Such a shame your mother didn’t swallow you {}.",
                "Take my lowest priority and put yourself beneath it, {}.",
                "The best part of {} ran down their mom’s leg.",
                "The only difference between {} and Hitler is Hitler knew when to kill himself.",
                "The only thing that will ever fuck {} is life.",
                "The smartest thing that ever came out of {}'s mouth was my dick.",
                "This is why everyone talks about {} as soon as they leave the room.",
                "Those aren’t acne scars, {}, those are marks from the coat hanger.",
                "Was your mother just in the bathroom {}? Because she forgot to flush your twin.",
                "{}, why are you playing hard to get when you’re so hard to want?",
                "You are a pizza burn on the roof of the world’s mouth.",
                "You are so ugly that when you were born, the doctor slapped your mother.",
                "You are the human embodiment of an eight-pound haircut.",
                "You are the stone in the shoes of humanity.",
                "You could fuck up a wet dream.",
                "You couldn’t organize a blowjob if you were in a Nevada brothel with a pocket full of hundred-dollar bills.",
                "You have more dick in your personality than you do in your pants.",
                "You have the charm and charisma of a burning orphanage.",
                "You know, people were right about you.",
                "You look like a bag of mashed-up assholes.",
                "You look like something I drew with my left hand.",
                "You look like the kind of person that buys condoms on his way to a family reunion.",
                "You look like two pounds of shit in a one-pound bag.",
                "You look like you were poured into your clothes but someone forgot to say when to stop.",
                "You look like your father would be disappointed in you if he stayed.",
                "You make me wish I had more middle fingers.",
                "You might want to get a colonoscopy for all that butthurt.",
                "You should put a condom on your head, because if you’re going to act like a dick you better dress like one, too.",
                "You smell like you wipe back to front.",
                "You suck dick at fucking pussy.",
                "You were birthed out your mother’s ass because her cunt was too busy.",
                "You’ll never be half the man your mother was.",
                "You’re a huge bag of tiny cocks.",
                "You’re about as important as a white crayon.",
                "You’re dumber than I tell people.",
                "You’re impossible to underestimate.",
                "You’re kinda like Rapunzel except instead of letting down your hair, you let down everyone in your life.",
                "You’re my favorite person besides every other person I’ve ever met.",
                "You’re not as dumb as you look.",
                "You’re not pretty enough to be that dumb.",
                "You’re not the dumbest person on the planet, but you sure better hope he doesn’t die.",
                "You’re so dense, light bends around you.",
                "You’re so inbred you’re a sandwich.",
                "You’re so stupid you couldn’t pour piss out of a boot if the directions were written on the heel.",
                "You’re the reason you mom swallows now.",
                "You’ve got a great body. Too bad there’s no workout routine for a face.",
                "You’ve gotta be two people, because no single person can be that stupid.",
                "Your birth certificate is an apology letter from the condom factory.",
                "Your face is so oily that I’m surprised America hasn’t invaded yet.",
                "Your face looks like it was set on fire and put out with chains.",
                "Your father should’ve wiped you on the sheets.",
                "Your mother fucks for bricks so she can build your sister a whorehouse.",
                "Your mother may have told you that you could be anything you wanted, but a douchebag wasn’t what she meant."
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