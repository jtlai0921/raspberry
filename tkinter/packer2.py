#!evn01/Scripts/python3.8
from tkinter import *


def interface(w):
    w.option_add("*font",('verdana',16))
    w.title("Pack - Example")
    w.geometry("600x200")


if __name__ == "__main__":
    window = Tk()
    interface(window)
    window.mainloop()

