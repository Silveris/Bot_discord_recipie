# imports
from dont_add import bot_info
import discord
from discord.ext import commands

# sets the bot up
client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print('The Chef has Arrived!')

#
# @client.event
# async def on_message(message):
#     if message.author == client:
#         return


@client.command()
async def chef_help(ctx):
    await ctx.send('''
    this bot is made to help aspiring chefs just like you!
    
    wip ------------- wip
    
    still figuring out what to put here. please give suggestions
    ''')
    return







# runs the bot
client.run(bot_info.token)