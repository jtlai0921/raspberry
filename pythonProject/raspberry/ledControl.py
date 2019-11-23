#!/usr/bin/python3.7
from gpiozero import LED
from time import sleep

if __name__ == "__main__":
    led = LED(25)
    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)