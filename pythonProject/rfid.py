from LCD.lcd_display import lcd
from time import sleep
from mfrc522 import MFRC522
from tkinter import *
from threading import Timer


class App:
    def __init__(self,window):
        self.uid = []
        self.preUid = []
        self.MIFAREReader = MFRC522()
        self.rfidHandler()

    def rfidHandler(self): #0.1秒執行一次
        reqStatus, tagType = self.MIFAREReader.MFRC522_Request(MFRC522.PICC_REQIDL)
        if reqStatus == MFRC522.MI_OK:
            scanStatus, self.uid = self.MIFAREReader.MFRC522_Anticoll()
            if scanStatus == MFRC522.MI_OK:
                if self.uid != self.preUid:
                    print(self.uid)
                    self.preUid = self.uid

        Timer(0.1, self.rfidHandler).start()







if __name__ == "__main__":
    window = Tk()
    window.title("RFID")
    window.option_add("*font", ("Helvetica", 18))
    app = App(window)
    window.mainloop()


