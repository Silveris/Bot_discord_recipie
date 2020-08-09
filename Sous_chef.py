# imports
from dont_add import bot_info
import discord
from discord.ext import commands
import sous_fns

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


@client.command()
async def chef_search_title(ctx, *, arg):
    results = 'empty'
    await ctx.send(f'''
    Searching for recipes that contain {arg} in the title. Give me a moment
    ''')
    results = sous_fns.search_by_title(arg)
    await ctx.send(f'''
        Results are as follows : 
        (if blank nothing was found)
    ''')
    for entry in results:
        await ctx.send(sous_fns.format_out_str(entry))

    return







# runs the bot
client.run(bot_info.token)