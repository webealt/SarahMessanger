# Declaratons
from utils import *
from UI import *

server = server()
client = server.client

"""
Functions

"""

"""
Events
"""
@client.event
async def on_ready():
    guild_count = 0

    for guild in client.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        guild_count = guild_count + 1

    print("Sarah Message Bot is in " + str(guild_count) + " guilds.")

    channel = client.get_channel(1122359614944587932)
    messages = [message async for message in channel.history(limit=5)]

    print(messages[0].content)

    await startUI(messages[0])
    exit()
    


# EVENT LISTENER FOR WHEN A NEW MESSAGE IS SENT TO A CHANNEL and DMs.
@client.event
async def on_message(message):
    if not message.guild:
        return
    elif message.channel.name == server.useChannel:
        if message.content[0] == "!":
            await msgChan(message, "Hello")

# starts bot
client.run(server.DISCORD_TOKEN)

#Get Last message

