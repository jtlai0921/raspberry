#!evn01/Scripts/python3.
from tkinter import *

if __name__ == "__main__":
    window = Tk()
    window.title("Pack-Example1")
    mainFrame = Frame(window)
    Button(mainFrame, text='Left', padx=10, pady=10).pack(side=LEFT)
    Button(mainFrame, text='Center', padx=10, pady=10).pack(side=LEFT)
    Button(mainFrame, text='Right', padx=10, pady=10).pack(side=LEFT)
    mainFrame.pack()
    window.mainloop()