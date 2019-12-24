#!evn01/Scripts/python3.8
""" docString"""
from tkinter import *


def interface(w):
    """ 建立介面 """
    w.option_add("*font",('verdana',16))
    w.title("Pack - Example")
    w.geometry("600x200")
    w.wm_resizable(height=False, width=False)



if __name__ == "__main__":
    window = Tk()
    interface(w=window)
    window.mainloop()

