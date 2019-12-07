#!/usr/bin/python3.7

from tkinter import *

def createInterface(w):
    mainFrame = Frame(w,width=300, height=110)
    xf = Frame(mainFrame, relief=GROOVE, borderwidth=2)
    Label(xf,text="You shot him!").pack(pady=10)
    Button(xf, text="He's dead!", state=DISABLED).pack(side=LEFT, padx=5, pady=8)
    Button(xf, text="He's completely dead!").pack(side=RIGHT, padx=5, pady=8)
    xf.place(relx=0.01, rely=0.125, anchor=NW)
    Label(mainFrame, text="self-defence against fruit").place(relx=0.6, rely=0.125, anchor=E)
    mainFrame.pack()

if __name__ == '__main__':
   window = Tk()
   createInterface(w=window)
   window.mainloop()
