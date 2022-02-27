import os
import random
from dotenv import load_dotenv

# 1
from discord.ext import commands

load_dotenv()
TOKEN = "OTQ3MTk2MjkxNDI1ODk0NTEx.YhpvSQ.Ax0n63Osp03i7eVWQ7iVMVd58PU"#os.getenv('DISCORD_TOKEN')

# 2
bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#The balls command
@bot.command(name='balls', help="balls.")
async def balls(ctx):
    response = "Balls."
    await ctx.send(response)

#Rolls dice command
@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll(ctx, number_of_dice: int, number_of_sides: int):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

#Join a voice channel
@bot.command(name = "join", pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("You aren't in a voice channel")

@bot.command(name= "leave", pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I leaved")

bot.run(TOKEN)