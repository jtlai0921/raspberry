from tkinter import *


class App:
    def __init__(self, master):
        Button(master, text='Left').pack(side=LEFT)
        Button(master, text='Center').pack(side=LEFT)
        Button(master, text='Right').pack(side=RIGHT)

if __name__ == '__main__':
    window = Tk()
    window.option_add('*font', ('verdana', 12, 'bold'))
    window.title('Pack - Example 1')
    display = App(window)
    window.mainloop()