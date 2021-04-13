from discord.ext import commands
from dotenv import load_dotenv
import os, ast

load_dotenv()

POKER_CATEGORY = int(os.getenv('POKER_CATEGORY'))
ADMIN_CATEGORY = int(os.getenv('ADMIN_CATEGORY'))
TEST_CATEGORY = int(os.getenv('TEST_CATEGORY'))
PREFIX = ast.literal_eval(os.getenv('PREFIX'))



def check_poker(ctx):
    
    return ctx.message.channel.category_id == POKER_CATEGORY and ctx.prefix == str(PREFIX[0])


def check_admin(ctx):

    return ctx.prefix == str(PREFIX[2])


def check_general(ctx):

    return ctx.message.channel.category_id != ADMIN_CATEGORY and ctx.message.channel.category_id != POKER_CATEGORY and ctx.message.channel.category_id != TEST_CATEGORY and ctx.prefix == str(PREFIX[1])
