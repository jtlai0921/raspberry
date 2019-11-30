#!/usr/bin/python3.7

from gpiozero import Button

if __name__ == "__main__":
    btn = Button(17)
    while True:
        if btn.is_active:
            print("按鈕被按");
        else:
            print("按鈕沒有被按")