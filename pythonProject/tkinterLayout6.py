from tkinter import *


class App:
    def __init__(self, master):
        frame = Frame(master)
        Button(frame, text='Left').pack(side=TOP, anchor=W, expand=YES, fill=BOTH)
        Button(frame, text='Center').pack(side=TOP, anchor=W, expand=YES, fill=BOTH)
        Button(frame, text='Right').pack(side=TOP, anchor=W, expand=YES, fill=BOTH)
        frame.pack(side=LEFT, expand=YES, fill=BOTH)

        frame1 = Frame(master)
        Button(frame1, text='Left').pack(side=LEFT, anchor=W, expand=YES, fill=BOTH)
        Button(frame1, text='Center').pack(side=LEFT, anchor=W, expand=YES, fill=BOTH)
        Button(frame1, text='Right').pack(side=LEFT, anchor=W, expand=YES, fill=BOTH)
        frame1.pack(side=RIGHT, expand=YES, fill=BOTH)

        frame2 = Frame(master)
        Label(frame2, text="First").grid(row=0, column=0, sticky=E)
        Label(frame2, text="Second").grid(row=1, column=0, sticky=E)
        frame2.pack(side=TOP, expand=YES, fill=BOTH)


if __name__ == '__main__':
    window = Tk()
    window.option_add('*font', ('verdana', 12, 'bold'))
    window.title('Pack - Example 1')
    window.geometry("300x300")
    display = App(window)
    window.mainloop()
