from LCD.lcd_display import lcd
from gpiozero import Buzzer
from time import sleep

my_lcd = lcd()
my_lcd.display_string("Raspberry Pi", 1)
my_lcd.display_string("Robert HSU", 2)
bz = Buzzer(16)
bz.on()
sleep(2)
bz.off()
sleep(2)