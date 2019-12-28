from LCD.lcd_display import lcd
from time import sleep
from mfrc522 import MFRC522

my_lcd = lcd()
my_lcd.display_string("Raspberry Pi", 1)
my_lcd.display_string("Robert HSU", 2)

