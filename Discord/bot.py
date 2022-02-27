# bot.py
import os

import discord
import random
import time
from dotenv import load_dotenv

#The discord bot token. This is special sauce
load_dotenv()
TOKEN = "OTQ3MTk2MjkxNDI1ODk0NTEx.YhpvSQ.BFXlJ1MuH_yfuVKhsCflvXAm7lU"#os.getenv('DISCORD_TOKEN')

#Sets up the client as the discord client
client = discord.Client()

#---------- EVENTS ----------#
# This section defines all the things that happen for the discord bot.
# Bots respond to "events"

#Message alert when someone joins the server
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

#DMs someone when they join in order to welcome them to the server
'''
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
'''

#Responds to a message with another message
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'balls?':
        response = "balls"
        #time.sleep(1)
        await message.channel.send(response)

    elif message.content == 'raise':
        raise discord.DiscordException



#The main code that starts the bot
client.run(TOKEN)