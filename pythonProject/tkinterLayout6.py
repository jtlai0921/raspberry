from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        Button(frame, text='Left').pack(side=TOP, anchor=W, expand=YES, fill=X)
        Button(frame, text='Center').pack(side=TOP, anchor=W, expand=YES, fill=X)
        Button(frame, text='Right').pack(side=TOP, anchor=W, expand=YES, fill=X)
        frame.pack(expand=YES, fill=X)


if __name__ == '__main__':
    window = Tk()
    window.option_add('*font', ('verdana', 12, 'bold'))
    window.title('Pack - Example 1')
    window.geometry("300x200")
    display = App(window)
    window.mainloop()
