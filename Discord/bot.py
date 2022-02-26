import os

import discord
from dotenv import load_dotenv

#dotenv is not being used because it didn't want to work for some reason
#Token is in plaintext for now, this will be updated later
load_dotenv()
TOKEN = "OTQ3MTk2MjkxNDI1ODk0NTEx.YhpvSQ.MIkprnp3bJJ7gz7xcZ5yYRecPPI"#os.getenv('DISCORD_TOKEN')

#defines the client that will be called
client = discord.Client()

#Creates the event and defines what it will do
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

#Runs the client and connects the bot to discord. When this runs, the bot will appear 'online' on discord
client.run(TOKEN)