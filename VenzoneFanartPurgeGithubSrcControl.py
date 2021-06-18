import discord 
from Token import *
from discord.ext import commands
from datetime import datetime

'''
THE IS WORKING EXECPET FOR DELETING EVERY 24 HRS
Test Doc
'''
client = discord.Client()
Channel_name = '💗-fanart'
msg_to_delete = []
Noon = 24*60
allowed_ids = {'3va':502253915463614477} #'Panda':635845590491725852 | 'Cool Kid':744455901011902484
del_msg = []







def Time_To_Noon():
    now = datetime.now()
    Current_Time = now.strftime("%H:%M:%S")
    Current_Time = Current_Time.split(':')
    time_in_sec = (int(Current_Time[0]) * 60) + (int(Current_Time[1])) + int(Current_Time[2])/60
    time_to_Noon = Noon - time_in_sec
    return time_to_Noon

bot_chan = client.get_channel(854812658985599006)
bot_chan.send('test')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    Channel = message.channel
    Author = message.author
    msg = await Channel.fetch_message(message.id)
    bot_chan = client.get_channel(854812658985599006)

    if Channel != client.get_channel(835641585777639434):
        return

    if message.attachments or message.reference: #if it's a reply or an attachment
        return

    if message.author == client.user: #if it's this bot thats typing messages
        return

    Roles = discord.utils.get(Author.roles, name = 'Mods')
    Roles = str(Roles)
    if Roles == 'Mods': #if a mod types the message
        if message.content == '!Del':
            for i in del_msg:
                await bot_chan.send(f'"{i.content}" by {i.author} was deleted')
                await i.delete()
            del_msg.clear()
            await bot_chan.send(f'<#835641585777639434> has been purged by {message.author.mention}')
            await message.delete()
        return

    for ids in allowed_ids: #if the person is allowed to type messages
        if message.author.id == allowed_ids[ids]:
            return
    del_msg.append(msg)

    time_to_next_delete = Time_To_Noon()*60

    if message.attachments or message.reference: #if it's a reply or an attachment
        return
    try:
        await message.delete(delay = time_to_next_delete)
    except:
        return



client.run(Token)