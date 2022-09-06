import os

from dotenv import load_dotenv
import discord
from colorama import Back,Fore,Style
import time
import platform
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.command()
async def hello(ctx):
    await ctx.send("Ola sou um bot chines ")

@client.event
async def on_ready():
    prfx = (Back.LIGHTBLACK_EX+Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE+ Style.BRIGHT)
    print(prfx + " Logged in as " + Fore.CYAN + client.user.name)
    print(prfx + " Bot Id " + Fore.CYAN + str(client.user.id))
    print(prfx + " Discord Version " + Fore.CYAN + discord.__version__)
    print(prfx + " Python Version " + Fore.CYAN + str(platform.python_version()))

client.run(TOKEN)
