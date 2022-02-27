from lib2to3.refactor import MultiprocessRefactoringTool
import os
import random
from dotenv import load_dotenv
import discord
from discord import FFmpegPCMAudio

# 1
from discord.ext import commands

load_dotenv()
TOKEN = "OTQ3MTk2MjkxNDI1ODk0NTEx.YhpvSQ.j5jZjJoi8aAMElAJ9zeMTTcvoHc"#os.getenv('DISCORD_TOKEN')

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

#Join the users voice channel on command
@bot.command(name = "join", pass_context = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('audio.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You aren't in a voice channel")

#Leave a voice channel on command
@bot.command(name= "leave", pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I leaved")
    else:
        await ctx.send("I isnt in voice")

#Rick
@bot.command(name = "rick", pass_context = True)
async def rick(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('audio.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You aren't in a voice channel")

#Pause
@bot.command(name = "pause", pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("There's no audio playing")

#Play
@bot.command(name = "resume", pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("There's no audio playing")

#Stop
@bot.command(name = "stop", pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()

#play
@bot.command(name = "play", pass_context = True)
async def stop(ctx, arg):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    source = FFmpegPCMAudio(arg)
    player = voice.play(source)


bot.run(TOKEN)