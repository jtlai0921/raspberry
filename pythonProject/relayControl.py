from tkinter import *
from gpiozero import LED as Relay
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


class App:
    def __init__(self, window):
        self.relay = Relay(25)

        #firebase initial
        cred =credentials.Certificate("/home/pi/Documents/certificate/raspberryfirebase-firebase-adminsdk-y4f0x-65514e121f.json")
        default_app = firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberryfirebase.firebaseio.com/'
})
        #interface
        self.buttonText = StringVar()

        mainFrame = Frame(window, borderwidth=2, relief=GROOVE)
        Button(mainFrame, textvariable=self.buttonText, command=self.userClick).pack(expand=YES, fill=BOTH, padx=40, pady=25)
        self.buttonText.set("OPEN")
        mainFrame.pack(expand=YES, fill=BOTH, padx=5, pady=20)

        self.relayControlRef = db.reference('iot1221/relayControl')
        self.relayControlRef.listen(self.firebaseDataChanges)

    def userClick(self):
        if self.relayControlRef.get():
            self.relayControlRef.set(False)
        else:
            self.relayControlRef.set(True)

    def firebaseDataChanges(self, event):
        print("Event Data:{},Event paht:{}".format(event.data, event.path))
        if event.data:
            self.buttonText.set("CLOSE")
        else:
            self.buttonText.set("OPEN")
        pass


if __name__ == "__main__":
    window = Tk()
    window.title("relayControl")
    window.geometry("300x200")
    window.option_add("*Font", ('verdana', 20))
    window.option_add('*Label.Font', ('verdana', 18))
    window.option_add('*Button.Background', "dark gray")
    app = App(window)
    window.mainloop()