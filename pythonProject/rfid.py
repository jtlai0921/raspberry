from LCD.lcd_display import lcd
from time import sleep
from mfrc522 import MFRC522
from tkinter import *

class App:
    def __init__(self,window):
        print(window.title)

if __name__ == "__main__":
    window = Tk()
    window.title("RFID")
    window.option_add("*font",("Helvetica", 18))
    app = App(window)
    window.mainloop()


