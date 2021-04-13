#!/bin/python3

import os, discord, ast
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
PREFIX = os.getenv('PREFIX')

intents = discord.Intents.default()
intents.members = True

# different prefixes for different command types and channels
bot = commands.Bot(intents=intents, command_prefix=ast.literal_eval(PREFIX))

cogs = [
    'cogs.admin.command_errors',
    'cogs.admin.server_admin',
    'cogs.general.user_commands',
    'cogs.general.quotes',
    'cogs.economy.stonks',
    'cogs.cards.poker_commands'
    ]

for ext in cogs:
    bot.load_extension(ext)
    print("Loaded Extension: {}".format(ext))


bot.run(TOKEN)