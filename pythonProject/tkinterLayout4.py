from tkinter import *

class App:
    def __init__(self, master):
        Button(master, text='Left').pack(side=TOP, expand=YES)
        Button(master, text='Center').pack(side=TOP, expand=YES)
        Button(master, text='Right').pack(side=TOP, expand=YES)

if __name__ == '__main__':
    window = Tk()
    window.option_add('*font', ('verdana', 12, 'bold'))
    window.title('Pack - Example 1')
    window.geometry("300x200")
    display = App(window)
    window.mainloop()