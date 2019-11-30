#!/usr/bin/python3.7

from tkinter import *

if __name__ == "__main__":
    master = Tk()
    ledBtn = Button(master)
    ledBtn.configure(text="You shot me!")
    ledBtn.pack()
    mainloop()

