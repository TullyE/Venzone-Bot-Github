import discord 
from Token import * #import all vars from Token.py (in this case only Token)
import asyncio, discord

client = discord.Client()
allowed_ids = {'3va':502253915463614477, 'Panda':635845590491725852} #, 'Cool Kid':744455901011902484}
del_msg = []

async def send_msg_every_24hrs():
    fanart_chan = client.get_channel(835641585777639434) #THE INT CAN BE CHANED THATS THE CHANNEL ID
    while True:
        await fanart_chan.send('!Del') #What you want to be sent 
        await asyncio.sleep(86400) #every x sec <<<86400>>> is the num of sec in 24hrs

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await send_msg_every_24hrs()

@client.event
async def on_message(message):
    roles = discord.utils.get(message.author.roles, name = 'Mods')
    mod = 'Mods' == str(roles)
    for ids in allowed_ids: #if the person is allowed to type messages
        if message.author.id == allowed_ids[ids]:
            mod = True
            break

    if message.channel == client.get_channel(835641585777639434): #If the message WAS sent in Fanart (The channel that's being purged)
        msg_id = await message.channel.fetch_message(message.id)
        del_msg_chan = client.get_channel(854812658985599006) #Channel where deleted messages are sent

        if message.attachments or message.reference: #if it's a reply or an attachment This is a boolean check<<<
            return

        if mod or message.author == client.user: #if a mod types the message
            if message.content == '!Del':
                for i in del_msg:
                    await del_msg_chan.send(f'"{i.content}" by {i.author} was deleted') #Keeps track of all deleted messages and their original senders
                    await i.delete()
                del_msg.clear()
                await del_msg_chan.send(f'<#835641585777639434> has been purged by {message.author.mention}') #Alerts that the channel was cleaned even if nothing was deleted
                await message.delete()
                return
            return       
        del_msg.append(msg_id)
        return

client.run(Token)