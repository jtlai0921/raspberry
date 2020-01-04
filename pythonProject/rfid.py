from LCD.lcd_display import lcd
from time import sleep
from mfrc522 import MFRC522
from tkinter import *
from threading import Timer


class App:
    def __init__(self,window):
        self.uid = []
        self.preUid0 = 0
        self.preUid1 = 0
        self.preUid2 = 0
        self.preUid3 = 0
        self.MIFAREReader = MFRC522()
        self.rfidHandler()

    def rfidHandler(self): #0.1秒執行一次
        status, tagType = self.MIFAREReader.MFRC522_Request(MFRC522.PICC_REQIDL)
        if status != MFRC522.MI_OK:
            print("狀態不是ok")
        else:
            print("狀態ok")
        Timer(0.1, self.rfidHandler).start()







if __name__ == "__main__":
    window = Tk()
    window.title("RFID")
    window.option_add("*font", ("Helvetica", 18))
    app = App(window)
    window.mainloop()


