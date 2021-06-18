import discord 
from discord import channel
import numpy as np
import string
import os
import string
from Token import *
from discord.ext import commands
from datetime import datetime

'''
AGAIN NOT WORKIGN BUT ALMOST
'''


bot = commands.Bot(command_prefix = '')
client = discord.Client()

Channel_name = '💗-fanart'
alphabet = string.ascii_lowercase
msg_to_delete = []
Noon = 24*60



def Time_To_Noon():
    now = datetime.now()
    Current_Time = now.strftime("%H:%M:%S")
    Current_Time = Current_Time.split(':')
    time_in_sec = (int(Current_Time[0]) * 60) + (int(Current_Time[1])) + int(Current_Time[2])/60
    Time_To_Noon = Noon - time_in_sec
    return Time_To_Noon

print(Time_To_Noon())

allowed_ids = {'3va':502253915463614477} #'Panda':635845590491725852 | 'Cool Kid':744455901011902484
del_msg = []

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
@client.event
async def on_message(message):
    TheMessage = message.content
    Channel = message.channel
    Author = message.author
    msg = await Channel.fetch_message(message.id)
    time_to_next_delete = Time_To_Noon()*60
    Check = False

    if Channel != Channel_name:
        print
        return

    if message.attachments or message.reference: #if it's a reply or an attachment
        return

    if message.author == client.user: #if it's this bot thats typing messages
        return

    Roles = discord.utils.get(Author.roles, name = 'Mods')
    Roles = str(Roles)
    if Roles == 'Mods': #if a mod types the message
        if TheMessage == '!Clean' or TheMessage == '!Del':
            Check = True
            for i in del_msg:
                await i.delete()
            del_msg.clear()
        return

    for ids in allowed_ids: #if the person is allowed to type messages
        if message.author.id == allowed_ids[ids]:
            return
    del_msg.append(msg)
    try:
        await message.delete(delay = time_to_next_delete)
        if Check == False:
            del_msg.clear()
    except:
        pass
client.run(Token)