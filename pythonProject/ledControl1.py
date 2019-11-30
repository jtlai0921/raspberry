#!/usr/bin/python3.7

from tkinter import *
from tkinter import Button
from gpiozero import LED

led = LED(25);

if __name__ == "__main__":
    master = Tk()
    master.title("LED 開關")
    Button(master, text="you shot me", padx=70, pady=30).pack(padx=20, pady=20)

    #led
    led.on()
    mainloop()

