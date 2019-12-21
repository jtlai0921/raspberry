from tkinter import *
from gpiozero import LED as Relay

class App:
    def __init__(self, window):
        self.relay = Relay(25)

if __name__ == "__main__":
    window = Tk()
    window.title("relayControl")
    window.geometry("300x200")
    window.option_add("*Font", ('verdana', 18, 'bold'))
    window.option_add('*Label.Font', ('verdana', 18))
    window.option_add('*Button.Background', "dark gray")
    app = App(window)
    window.mainloop()