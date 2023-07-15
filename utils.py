import discord
import os
from dotenv import load_dotenv
load_dotenv()

"""
Classes
"""
# private variables to allow functions below to share same client
_intents = discord.Intents.all()
_client = discord.Client(intents=_intents)


class server:
    def __init__(self):
        self.client = _client
        self.useChannel = "sarah-message"  # <-- Channel to point the bot too
        self.DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")


"""
Functions
--> msgChan(message: message object, text: text to send) /// Send message to channel using their message in channel as user reference
--> msgDm(message: message object, text: text to send) /// Dm user using their message in channel as user reference
"""


async def msgChan(message, text):
    await message.channel.send(text)


async def msgDm(message, text):
    user = _client.get_user(message.author.id)
    await user.send(text)
