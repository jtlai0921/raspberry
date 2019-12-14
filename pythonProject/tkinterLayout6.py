from tkinter import *


class App:
    def __init__(self, master):

        frame2 = Frame(master)
        Label(frame2, text="First").grid(row=0, column=0, sticky=E)
        Label(frame2, text="Second").grid(row=1, column=0, sticky=E)
        Entry(frame2).grid(row=0, column=1)
        Entry(frame2).grid(row=1, column=1)
        Checkbutton(frame2, text='Preserve aspec').grid(row=2, column=0, columnspan=2, sticky=W)
        photo = PhotoImage(file='images.gif')
        label = Label(image=photo)
        label.image = photo
        label.grid(row=0, column=2, rowspan=2)
        frame2.pack(side=BOTTOM, expand=YES, fill=BOTH)


if __name__ == '__main__':
    window = Tk()
    window.option_add('*font', ('verdana', 12, 'bold'))
    window.title('Pack - Example 1')
    window.geometry("300x300")
    display = App(window)
    window.mainloop()
