# bot.py
import os

import discord
import random
import time
from dotenv import load_dotenv

load_dotenv()
TOKEN = "OTQ3MTk2MjkxNDI1ODk0NTEx.YhpvSQ.5CJjJhJsA5C2U_I82PaYbShWPCY"#os.getenv('DISCORD_TOKEN')


client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

'''
@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
'''

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'Balls. Nuts even!'
    ]

    if message.content == 'balls?':
        response = random.choice(brooklyn_99_quotes)
        time.wait(3)
        await message.channel.send(response)



client.run(TOKEN)

'''


class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

client = CustomClient()
client.run(TOKEN)
'''

'''
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run(TOKEN)
'''