from tkinter import *
import tkinter as tk
import tkinter.font as font
import requests
import webbrowser
import os
from datetime import date
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import imghdr

async def startUI(message):
    #download function
    path = os.path.join(os.getcwd(), str(date.today()))
    if not os.path.exists(path): os.mkdir(path)
    def dlAttach(status):
        openExplorer = False
        for atc in message.attachments:
            url = atc.url
            filename = path + "\\" + url.split('/')[-1]
            #download files
            r = requests.get(url, allow_redirects=True)
            open(filename, 'wb').write(r.content)
            
            #open
            if imghdr.what(filename) in ['jpeg', 'jpg', 'png']:
                plt.figure(url.split('/')[-1])
                plt.axis('off')
                image = mpimg.imread(filename)
                plot = plt.imshow(image)
            else:
                openExplorer = True

        status.delete(1.0, tk.END)
        status.insert(tk.END, "Attachments downloaded!\nCheck: " + path)

        if openExplorer: webbrowser.open("file:///" + path)
        plt.show()

    # Creating the tkinter window
    root = Tk()
    root.geometry("750x380")

    #fonts
    buttonFont = font.Font(size = 14, family = 'Segoe UI', weight = 'bold')
    labelFont = font.Font(size = 20, family = 'Terminal', weight = 'bold')
    textFont = font.Font(size = 12, family = 'Courier')

    # Add a Scrollbar(horizontal)
    #v=Scrollbar(root, orient='vertical')
    #v.pack(side=RIGHT, fill='y')

    #message
    l = Label(root, text = "Sarah Messenger v1.0")
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




