#!/usr/bin/python3.7
'''
這是製作文件的地方
'''
from tkinter import Tk
from tkinter import Frame
from tkinter import Label
from tkinter.constants import *

if __name__ == "__main__":
    root = Tk()
    root.title("LED Control")
    for relief in [RAISED, SUNKEN, FLAT, RIDGE, GROOVE, SOLID]:
        f = Frame(root, borderwidth=2, relief=relief)
        Label(f, text=relief, width=10).pack(side=LEFT)
        f.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()