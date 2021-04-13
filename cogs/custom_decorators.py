from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

POKER_CATEGORY = os.getenv('POKER_CATEGORY')
ADMIN_CATEGORY = os.getenv('ADMIN_CATEGORY')
TEST_CATEGORY = os.getenv('TEST_CATEGORY')



def check_poker(ctx):
    
    return ctx.message.channel.category_id == POKER_CATEGORY and ctx.prefix == '$' 


def check_admin(ctx):

    return ctx.message.channel.category_id == ADMIN_CATEGORY and ctx.prefix == "+"


def check_general(ctx):

    return ctx.message.channel.category_id != ADMIN_CATEGORY and ctx.message.channel.category_id != POKER_CATEGORY and ctx.message.channel.category_id != TEST_CATEGORY and ctx.prefix == "!"
