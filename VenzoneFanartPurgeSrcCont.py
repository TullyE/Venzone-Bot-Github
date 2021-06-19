import discord 
from Token import * #import all vars from Token.py (in this case only Token)
import asyncio, discord

client = discord.Client()
allowed_ids = {'Venbot':853822944510083083, 'Dino':740111453041983540, 'Venzai':707507650933555300} #Add user ID's.. doing so allows their messages to not get purged
del_msg = []

async def send_msg_every_24hrs():
    fanart_chan = client.get_channel(775788393769992222) #THE INT CAN BE CHANED THATS THE CHANNEL ID
    while True:
        await fanart_chan.send('/Del') #What you want to be sent 
        await asyncio.sleep(86400) #every x sec <<<86400>>> is the num of sec in 24hrs

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await send_msg_every_24hrs()

@client.event
async def on_message(message):
    roles = discord.utils.get(message.author.roles, name = 'Artist!')
    mod = 'Artist!' == str(roles)
    for ids in allowed_ids: #if the person is allowed to type messages
        if message.author.id == allowed_ids[ids]:
            mod = True
            break
    if message.content == '/Youtube':
        await message.channel.send('https://www.youtube.com/venzai')       
    if message.channel == client.get_channel(775788393769992222): #If the message WAS sent in Fanart (The channel that's being purged)
        msg_id = await message.channel.fetch_message(message.id)
        del_msg_chan = client.get_channel(855613510746243083) #Channel where deleted messages are sent

        if message.attachments or message.reference: #if it's a reply or an attachment This is a boolean check<<<
            return

        if mod or message.author == client.user: #if a mod types the message
            if message.content == '/Del':
                embed = discord.Embed()
                embed.title = f'{len(del_msg)} Messages have been deleted.'
                embed.description = ''
                #for i in del_msg:
                #    await del_msg_chan.send(f'"{i.content}" by {i.author} was deleted') #Keeps track of all deleted messages and their original senders
                #    await i.delete()
                for i in del_msg:
                    embed.description += f'\nFrom {i.author}\n{i.content}\n'
                    await i.delete()
                del_msg.clear()
                await message.delete()
                try:
                    await del_msg_chan.send(embed = embed)
                except:
                    embed = discord.Embed()
                    embed.title = f'{len(del_msg)} Messages have been deleted.'
                    embed.description = ''
                    await del_msg_chan.send(embed = embed)
                await del_msg_chan.send(f'<#775788393769992222> has been purged by {message.author.mention}') #Alerts that the channel was cleaned even if nothing was deleted
                return
            return       
        del_msg.append(msg_id)
        return

client.run(Token)