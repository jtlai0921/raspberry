#!/usr/bin/python3.7

from tkinter import *
from tkinter import Button
from gpiozero import LED

led = LED(25);
def userClick():
    if led.is_active:
        led.off()
    else:
        led.on()

if __name__ == "__main__":
    master = Tk()
    master.title("LED 開關")
    frame = Frame(master, borderwidth=2, relief=GROOVE)
    Button(frame, text="you shot me", padx=70, pady=30, command=userClick).pack(padx=20, pady=20)
    frame.pack(padx=10, pady=10)
    mainloop()

