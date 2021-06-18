import discord 
from Token import *
from discord.ext import commands
import asyncio, discord

client = discord.Client()
allowed_ids = {'3va':502253915463614477, 'Panda':635845590491725852} #, 'Cool Kid':744455901011902484}
del_msg = []

async def my_background_task():
    Fanart_Chan = client.get_channel(835641585777639434) #THE INT CAN BE CHANED THATS THE CHANNEL ID
    while True:
        await Fanart_Chan.send('!Del') #What you want to be sent 
        await asyncio.sleep(86400) #every x sec

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await my_background_task()

@client.event
async def on_message(message):

    Channel = message.channel
    Author = message.author

    if Channel == client.get_channel(835641585777639434): #If the message WAS sent in Fanart (The channel that's being purged)
        msg_id = await Channel.fetch_message(message.id)
        del_msg_chan = client.get_channel(854812658985599006) #Channel where deleted messages are sent

        if message.attachments or message.reference: #if it's a reply or an attachment >>>This is a boolean check<<<
            return

        Roles = discord.utils.get(Author.roles, name = 'Mods')
        Roles = str(Roles)
        if Roles == 'Mods' or message.author == client.user: #if a mod types the message
            if message.content == '!Del':
                for i in del_msg:
                    await del_msg_chan.send(f'"{i.content}" by {i.author} was deleted')
                    await i.delete()
                del_msg.clear()
                await del_msg_chan.send(f'<#835641585777639434> has been purged by {message.author.mention}')
                await message.delete()
            return

        for ids in allowed_ids: #if the person is allowed to type messages
            if message.author.id == allowed_ids[ids]:
                return

        if message.author == client.user: #if it's this bot thats typing messages
            return
        
        del_msg.append(msg_id)
        return

client.run(Token)