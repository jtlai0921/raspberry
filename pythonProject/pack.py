#!/usr/bin/python3.7

from tkinter import *

def createInterface(w):
    mainFrame = Frame(w,width=300, height=110)
    mainFrame.pack()

if __name__ == '__main__':
   window = Tk()
   createInterface(w=window)
   window.mainloop()
