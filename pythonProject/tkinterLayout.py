from tkinter import *
from tkinter import Tk


class App:
    def __init__(self, master):
        Button(master, text='left').pack(side=LEFT)
        Button(master, text='Center').pack(side=LEFT)
        Button(master, text='Right').pack(side=LEFT)


if __name__ == "__main__":
    window = Tk()
    window.title("Pack - Example 1")
    display = App(window)
    window.mainloop()
