import os

from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


@client.command()
async def hello(ctx):
    await ctx.send("Hello")


client.run(TOKEN)
