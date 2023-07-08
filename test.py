from tkinter import *
  
# Creating the tkinter window
root = Tk()
root.geometry("200x100")
  
# Button for closing
exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.pack(pady=20)
  
root.mainloop()
