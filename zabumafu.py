#Bot.py
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
import creds
import asyncio

TOKEN = creds.token

bot = commands.Bot(command_prefix=";")

async def on_ready():
    print ("Ret to Go")

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command()
async def leave(ctx):
    server = ctx.message.guild.voice_client
    channel = ctx.channel
    await server.disconnect()

@bot.command(pass_context=True)
async def ping(ctx):
    channel = ctx.channel
    await channel.send('Pong')

bot.run(TOKEN)