import os
from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv


def setup():
    load_dotenv()
    token = os.getenv('DISCORD_TOKEN')
    intents = Intents.all()
    bot = commands.Bot(command_prefix='!', intents=intents)
    return bot, token


BOT, TOKEN = setup()


@BOT.command(name='gg', help='placeholder')
async def gg(ctx, game=None, time=None):
    try:
        resp = "gg command"
        await ctx.send(resp)
    except Exception as e:
        await ctx.send(e)


@BOT.command(name='register', help='placeholder')
async def register(ctx):
    try:
        resp = "register command"
        await ctx.send(resp)
    except Exception as e:
        await ctx.send(e)


BOT.run(TOKEN)
