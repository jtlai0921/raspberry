#!evn01/Scripts/python3.8
""" docString"""
from tkinter import *


def interface(w):
    """ 建立介面 """
    w.option_add("*font",('verdana',16))
    w.title("Pack - Example")
    w.geometry("600x200")
    w.wm_resizable(height=False, width=False)

    menuFrame = Frame(w,bg='purple',width=200)
    lineFrame = Frame(menuFrame,borderwidth=2,relief=GROOVE,width=200,bg='purple')
    lineFrame.pack(expand=YES, fill=BOTH,padx=10,pady=10)
    menuFrame.pack(side=LEFT, expand=YES,fill=BOTH)

    rightFrame = Frame(w, bg='gray',width=400)

    rightFrame.pack(side=LEFT, expand=YES, fill=BOTH)



if __name__ == "__main__":
    window = Tk()
    interface(w=window)
    window.mainloop()

