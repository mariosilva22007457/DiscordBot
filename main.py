"""
        # TODO: LIST


# TODO: < RESOLVER BUGS >
# TODO: <Facilitar , melhorar interface>


"""

import os
from random import random
from random import choice
from discord.ext.commands import bot
from dotenv import load_dotenv
import discord
from colorama import Back, Fore, Style
import time
import platform
from discord.ext import commands
import json
import requests

import random

print(random.__file__)
load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(
    command_prefix='!',
    intents=discord.Intents.all()
)

# Discord Channel ID
channel_ID = 837870956781109258


@client.command()
async def hello(ctx):
    await ctx.send("Ola sou um bot chines")


@client.event
async def on_ready():
    prfx = (
            Back.LIGHTBLACK_EX
            + Fore.GREEN
            + time.strftime("%H:%M:%S UTC", time.gmtime())
            + Back.RESET
            + Fore.WHITE
            + Style.BRIGHT
    )
    print(prfx + " Logged in as " + Fore.CYAN + client.user.name)
    print(prfx + " Bot Id " + Fore.CYAN + str(client.user.id))
    print(prfx + " Discord Version " + Fore.CYAN + discord.__version__)
    print(prfx + " Python Version " + Fore.CYAN + str(platform.python_version()))


@client.command(aliases=['close', 'stop'])
async def shutdown(ctx):
    await ctx.send("Shutting down the bot")
    await client.close()


@client.command(aliases=['uinfo', 'whois'])
async def userinfo(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.message.author

    discord_USER_ROLES = [role for role in member.roles]

    bot_USER_OUTPUT_INFOS = discord.Embed(
        title="User info", description=f"User info on the user {member.name}",
        color=discord.Color.green(), timestamp=ctx.message.created_at
    )

    bot_USER_OUTPUT_INFOS.set_thumbnail(
        url=member.avatar
    )

    bot_USER_OUTPUT_INFOS.add_field(
        name="ID", value=member.id
    )

    bot_USER_OUTPUT_INFOS.add_field(
        name="Name", value=f"{member.name}#{member.discriminator}"
    )

    bot_USER_OUTPUT_INFOS.add_field(
        name="Nickname", value=member.display_name
    )

    bot_USER_OUTPUT_INFOS.add_field(
        name="Status", value=member.status
    )

    bot_USER_OUTPUT_INFOS.add_field(
        name="Created at ", value=member.created_at.strftime("%a, %B %#d, %Y, %I:%M %p ")
    )

    bot_USER_OUTPUT_INFOS.add_field(
        name="Joined at ", value=member.joined_at.strftime("%a, %B %#d, %Y, %I:%M %p ")
    )

    bot_USER_OUTPUT_INFOS.add_field(
        name=f"Roles ({len(discord_USER_ROLES)})", value=" ".join([role.mention for role in discord_USER_ROLES])
    )

    bot_USER_OUTPUT_INFOS.add_field(
        name="Top Role", value=member.top_role.mention
    )

    # embed.add_field(
    # name="Messages", value="007"
    # )

    bot_USER_OUTPUT_INFOS.add_field(
        name="Bot?", value=member.bot
    )

    await ctx.send(embed=bot_USER_OUTPUT_INFOS)


@client.event
async def on_member_join(member):
    import requests

    url = "https://joke3.p.rapidapi.com/v1/joke/%7Bid%7D/%7Bproperty%7D"

    headers = {
        "X-RapidAPI-Key": "280e7103fbmsh98c73bfa809efd1p1c9648jsn6e8c0153f599",
        "X-RapidAPI-Host": "joke3.p.rapidapi.com"
    }

    response = requests.request(
        "GET", url, headers=headers
    )

    channel = client.get_channel(channel_ID)

    await channel.send(
        "Welcome!" + f" {member.display_name} "
    )

    await channel.send(
        json.loads(response.text)['content']
    )


@client.event
async def on_member_remove(member):
    channel_REMOVED_USER = client.get_channel(channel_ID)

    await channel_REMOVED_USER.send(
        "Goodbye!" + f" {member.display_name} "
    )


#  Já funciona

@client.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [str(random.choice(range(1, number_of_sides + 1)))
            for _ in range(number_of_dice)]
    await ctx.send(', '.join(dice))


""""
    #API QUE DEMONSTRA AS CURRENCIES
    

import requests

url = "https://api.apilayer.com/exchangerates_data/latest?symbols={symbols}&base={base}"

payload = {}
headers= {
  "apikey": "CaZLiWDEvrEuh4Ot02XeR4fSYZpS6qBt"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
                
"""



# TODO: < TESTAR BUGS >
# TODO: <Facilitar , melhorar interface>
@client.command(name='convert', help='Converts x amount in a currency to another')
async def money(ctx,  amount: int,fromCurrency, toCurrency,):
    import requests
    url = 'http://data.fixer.io/api/latest?access_key=7370ff2962d49abefc56c32f5bc74aa8'
    response = requests.get(url)
    rate = response.json()['rates'][fromCurrency]
    amount_total = amount / rate
    amount_final = amount_total* (response.json()['rates'][toCurrency])
    amount_final = round(amount_final,3)
    await ctx.send(f"{amount} {fromCurrency} is {amount_final} {toCurrency}")


client.run(TOKEN)
