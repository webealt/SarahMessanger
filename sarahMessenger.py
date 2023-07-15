import os
from tkinter import *
import tkinter as tk
import tkinter.font as font
import requests
import webbrowser
import os
from datetime import date
import discord
from dotenv import load_dotenv
load_dotenv()

'''
functions
'''
async def startUI(message):
    #download function
    
    def dlAttach(status):
        path = os.path.join(os.getcwd(), str(date.today()))
        if not os.path.exists(path): os.mkdir(path)

        with open(path + "\\" + "Message.txt", "w") as text_file:
            text_file.write(message.content)

        for atc in message.attachments:
            url = atc.url
            filename = path + "\\" + url.split('/')[-1]
            #download files
            r = requests.get(url, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            
            #open
            webbrowser.open("file:///" + path)

        status.delete(1.0, tk.END)
        status.insert(tk.END, "Attachments downloaded!\nCheck: " + path)
    

    # Creating the tkinter window
    root = Tk()
    root.geometry("750x380")

    #fonts
    buttonFont = font.Font(size = 14, family = 'Segoe UI', weight = 'bold')
    labelFont = font.Font(size = 20, family = 'Terminal', weight = 'bold')
    textFont = font.Font(size = 12, family = 'Courier')

    #message
    l = Label(root, text = "Sarah Messenger v1.1")
    l['font'] = labelFont
    l.pack()

    #Text Box
    T = Text(root, height = 10, width = 65)
    T['font'] = textFont
    T.pack()
    T.insert(tk.END, message.content)

    #Number of Attachments Message
    A = Text(root, height = 2, width = 65)
    A['font'] = textFont
    A.pack(pady=5)
    A.insert(tk.END, "This message has " + str(len(message.attachments)) + " attachments.")

    # Button for closing
    down_button = Button(root, text="Download Attachments", command=lambda: dlAttach(A), height = 1, width = 20, bg = '#d3d3d3', fg = '#000000')
    down_button['font'] = buttonFont
    down_button.pack(pady=5)

    # Button for closing
    exit_button = Button(root, text="Exit", command=root.destroy, height = 1, width = 20, bg = '#ffcccb', fg = '#000000')
    exit_button['font'] = buttonFont
    exit_button.pack(pady=5)
  
    root.mainloop()

async def getMessage(message):
    content = message.content
    attachments = message.attachments
    return content, attachments

"""
Events
"""
_intents = discord.Intents.all()
_client = discord.Client(intents=_intents)
client = _client

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
    os._exit(0)

# starts bot
client.run(os.getenv("DISCORD_TOKEN"))