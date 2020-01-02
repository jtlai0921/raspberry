#!env01/Scripts/python3
from tkinter import *


def createrInterface(w):
    var = IntVar()
    items = [('Passion fruit',1), ('Loganberries', 2), ('Mangoes in syrup', 3), ('Oranges', 4),('Apples', 5),('Grapefruit', 6)]
    for text, value in items:
        Radiobutton(w,text = text, value = value, variable=var).pack(anchor=W)
    var.set(3)


if __name__ == '__main__':
    window = Tk()
    window.title("RadioButton")
    createrInterface(window)
    window.mainloop()