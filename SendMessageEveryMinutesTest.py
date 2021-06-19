import discord 
from discord.ext import commands
from datetime import datetime
import asyncio, discord
import os
from dotenv import load_dotenv
load_dotenv() #take envirment variables from .env

'''
Code adapted from https://stackoverflow.com/questions/61366148/python-discord-py-bot-interval-message-send
This was to test for the venzone bot
'''

import asyncio, discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".") # If you don't want a prefix just take out the parameter.

async def my_background_task():
    channel = discord.Object(id='854812658985599006')
    while True:
        await channel.send("TEST")
        await asyncio.sleep(5) # task runs every 60 seconds

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await my_background_task()

client.run(os.environ.get('DiscordToken'))