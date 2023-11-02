# https://realpython.com/how-to-make-a-discord-bot-python/
# bot.py
import os

import discord
#from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'cobalt':
        response = 'searching for cobalt strike...'
        await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'whoami':
        response = 'I am cobaltstrike hunter bot...'
        await message.channel.send(response)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'search' in message.content.lower():
        response = 'searching for cobalt strike...'
        await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'ram' in message.content.lower():
        response = 'searching RAM memory regions for cobalt strike...'
        await message.channel.send(response)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'uname' in message.content.lower():
        await message.channel.send('CobaltHunter 2.3.4')

client.run(TOKEN)

