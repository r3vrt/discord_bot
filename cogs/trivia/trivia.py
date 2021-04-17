import requests
import discord
import base64
from . import prepare_quiz
#from .. import custom_decorators
from discord.ext import commands

req = requests.get("https://opentdb.com/api_token.php?command=request")
data = req.json()
token = data['token']

class Trivia(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='trivia',
    brief='Random trivia questions',
    description='This command will start a list of 10 random questions')
    async def start_trivia(self, ctx):

        pass

        
        
        
        # question_bank = prepare_quiz.get_questions

        # if question_bank['response_code'] in [3, 4]:
            
        #     print("Requesting new token")
        #     token = pq.get_new_token()
        #     question_bank = pq.get_questions()


        # for cat in question_bank['results']:
        #     await ctx.send(str(base64.b64decode(cat['question']), "utf-8")))