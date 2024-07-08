# bot.py
import os
import discord
from discord.ext import commands, tasks
from discord.utils import get
intents = discord.Intents.default()
intents.members = True

from dotenv import load_dotenv, find_dotenv

load_dotenv()

#TOKEN and GUILD are pulled from .env file in this directory
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():

    for guild in client.guilds:
        if guild.name == GUILD:
            break
    
    members = '\n - '.join([member.name for member in guild.members])
    print(f'{guild.member_count} Guild Members:\n - {members}')

    guild = discord.utils.get(client.guilds, name="Py-Bot's server")

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
        )
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome! :)'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    muffin_key ="muffin"

    if message.content == "muffin":
        response = muffin_key
        await message.channel.send(response)
client.run(TOKEN)