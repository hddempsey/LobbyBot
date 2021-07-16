import os
import discord
from discord import player
from discord.ext import commands
from discord.ext.commands import Context
from lobby import Lobby, LobbyManager

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')

manager = LobbyManager()

@bot.command()
async def host(ctx: Context, game_name: str, num_players: int):
    try:
        create_lobby_response = manager.create_lobby(game=game_name, num_players=num_players)
        await ctx.send(create_lobby_response)

        add_player_response = manager.add_player(game=game_name, player=ctx.author)
        await ctx.send(add_player_response)
    except Exception as e:
        await ctx.send(e)

@bot.command()
async def join(ctx: Context, game_name):
    try:
        add_player_response = manager.add_player(game=game_name, player=ctx.author)
        await ctx.send(add_player_response)
    except Exception as e:
        await ctx.send(e)

bot.run(TOKEN)