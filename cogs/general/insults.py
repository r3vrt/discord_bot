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
                "{} is a pizza burn on the roof of the world’s mouth.",
                "{} is so ugly that when they were born, the doctor slapped their mother.",
                "{} is the human embodiment of an eight-pound haircut.",
                "{} is the stone in the shoes of humanity.",
                "{} could fuck up a wet dream.",
                "{} couldn’t organize a blowjob if they were in a Nevada brothel with a pocket full of hundred-dollar bills.",
                "{} has more dick in their personality than they do in their pants.",
                "{} has the charm and charisma of a burning orphanage.",
                "You know, people were right about {}.",
                "{} looks like a bag of mashed-up assholes.",
                "{} looks like something I drew with my left hand.",
                "{} looks like the kind of person that buys condoms on their way to a family reunion.",
                "{} looks like two pounds of shit in a one-pound bag.",
                "{} looks like they were poured into their clothes but someone forgot to say when to stop.",
                "{}, looks like your father would be disappointed in you if he stayed.",
                "{} makes me wish I had more middle fingers.",
                "{} might want to get a colonoscopy for all that butthurt.",
                "{} should put a condom on their head, because if they’re going to act like a dick they better dress like one, too.",
                "{} smells like they wipe back to front.",
                "{} sucks dick at fucking pussy.",
                "{} was birthed out their mother’s ass because her cunt was too busy.",
                "{}, you will never be half the man your mother was.",
                "You’re a huge bag of tiny cocks, {}.",
                "{} is about as important as a white crayon.",
                "{} is dumber than I tell people.",
                "{} is impossible to underestimate.",
                "{} is kinda like Rapunzel except instead of letting down their hair, they let down everyone in their life.",
                "{} is my favorite person besides every other person I’ve ever met.",
                "{} is not as dumb as they look.",
                "{} is not pretty enough to be that dumb.",
                "{} is not the dumbest person on the planet, but you sure better hope he doesn’t die.",
                "{} is so dense, light bends around them.",
                "{} is so inbred they’re a sandwich.",
                "{} is so stupid they couldn’t pour piss out of a boot if the directions were written on the heel.",
                "{} is the reason their mom swallows now.",
                "{} has got a great body. Too bad there’s no workout routine for a face.",
                "{} has gotta be two people, because no single person can be that stupid.",
                "{}'s birth certificate is an apology letter from the condom factory.",
                "{}'s face is so oily that I’m surprised America hasn’t invaded yet.",
                "{}'s face looks like it was set on fire and put out with chains.",
                "{}'s father should’ve wiped them on the sheets.",
                "{}'s mother fucks for bricks so she can build their sister a whorehouse.",
                "{}'s mother may have told them that they could be anything they wanted, but a douchebag wasn’t what she meant."
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