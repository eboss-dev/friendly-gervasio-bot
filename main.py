from apikeys import *
import discord
from time import sleep
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    '''
    #   In questo modo andiamo a leggere i messaggi
    #   potremmo anche vedere chi ha i permessi per
    #   usarli e SOLO in quel caso avere la capacità di
    #   cambiare in un determinato canale
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    '''

    #   Con questo comando entra nel primo voice channel
    #   e fa partire il suono
    if message.content.startswith('$countDown'):
        channel = client.get_channel(1015272924896309268)
        print("Countdown visto nella chat")
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="ps1.mp3"))
        # Sleep while audio is playing.
        while vc.is_playing():
            sleep(.1)
        await vc.disconnect()

client = commands.Bot(command_prefix='*', intents=intents)

@client.command()
async def join(ctx, member: discord.Member):  # This command will be named kill and will take two arguments: ctx (which is always needed) and the user that was mentioned
    channel = client.get_channel(1015272924896309268)
    print("Countdown visto nella chat")
    vc = await channel.connect()
    vc.play(discord.FFmpegPCMAudio(executable="C:/FFMPEG/ffmpeg.exe", source="ps1.mp3")
        ,after=lambda _: asyncio.run_coroutine_threadsafe(
        coro=vc.disconnect(),
        loop=vc.loop))
    # Sleep while audio is playing.
    #while vc.is_playing():
    #    sleep(.1)


@client.command()
async def test(ctx):
    role = discord.utils.get(ctx.guild.roles, name="Admin") # Get the role
    if role in ctx.author.roles: # Check if the author has the role
        await ctx.send("You can do this")
    else:
        await ctx.send("You do not have the `Admin` role.")
client.run(BOTTOKEN)
