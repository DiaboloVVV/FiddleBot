import discord
from giveaway.main_giveaway import *
from os import *
import sys,traceback
from discord.ext import commands
from dotenv import load_dotenv
from giveaway.main_giveaway import dbcreate
# from stay_alive import keep_alive

load_dotenv()

client = commands.Bot(command_prefix="$")

def extFiles():
    extlist = next(os.walk('.'))[1]
    if '.idea' in extlist and '.git' in extlist:
        extlist.pop(extlist.index('.idea'))
        extlist.pop(extlist.index('.git'))
    return extlist


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('with ravens..'))
    print('Has been logged in as {0.user}'.format(client))
    # dbcreate()


@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    extlist =extFiles()
    for name in extlist:
        try:
            client.load_extension(f'{name}.{extension}')
        except:
            pass


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    extlist = extFiles()
    for name in extlist:
        try:
            client.unload_extension(f'{name}.{extension}')
        except:
            pass


@client.command()
@commands.has_permissions(administrator=True)
async def reload(ctx):
    extlist = extFiles()
    for name in extlist:
        try:
            for filename in os.listdir(f'./{name}'):
                if filename.endswith('.py'):
                    client.unload_extension(f'{name}.{filename[:-3]}')
            for filename in os.listdir(f'./{name}'):
                if filename.endswith('.py'):
                    client.load_extension(f'{name}.{filename[:-3]}')
        except:
            pass


if __name__ == '__main__':
    extlist = extFiles()
    for name in extlist:
        try:
            for filename in os.listdir(f'./{name}'):
                if filename.endswith('.py'):
                    client.load_extension(f'{name}.{filename[:-3]}')
        except:
            pass
    # fixupdate()
    # keep_alive()
    # client.run('')
    client.run(os.environ['TOKEN'])
