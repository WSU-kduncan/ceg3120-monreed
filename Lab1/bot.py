# Based on example https://discordpy.readthedocs.io/en/stable/quickstart.html
import os

import discord
import random
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.message_content = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    parenttrap_quotes = [
        "Let me see... I know how to fence and you don't? Or, I have class and you don't? Take your pick.",
        'Look at me Martin, have you ever seen me like this?! No, don’t answer that.',
        'Oh, I would pay big money to see that woman climb a mountain.',
        'If you ask me the bouquet is a little too robust for a Merlot, but then again I am partial to the softer California grape.',
        'I have a brilliant beyond brilliant idea!',
        'Being young and beautiful isn’t a crime, you know.',
        "Oh, don't do this to me. I'm already seeing double.",
        ]
    if message.content == 'trap!':
    #if message.content.startswith('$trap'):
        response = random.choice(parenttrap_quotes)
        await message.channel.send(response)

client.run(TOKEN)
