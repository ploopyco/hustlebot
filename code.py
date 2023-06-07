import board
import digitalio
import usb_hid
import time
import random
import li
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

led.value = True

time.sleep(10)

skip = random.randrange(1, 50000)

while True:
    for char in li.lorum_ipsum:
        if skip != 0:
            skip = skip - 1
            continue

        try:
            keyboard_layout.write(char)

            st = random.uniform(0.1, 0.6)
            time.sleep(st)
        except:
            pass
