import time
import board
import mfrc522
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
import neopixel



##### KEYBOARD SETTINGS
## SUBSTITUTE WITH YOUR PREFERRED KEYBOARD LAYOUT
## https://www.neradoc.me/layouts/

import keyboard_layout_win_ic
from keycode_win_ic import Keycode
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = keyboard_layout_win_ic.KeyboardLayout(keyboard)



##### LED SETTINGS
#COLOR DEFINITIONS#
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0,0,0)



# VALUES TO SET FOR LED#
pixel_pin = board.GP20 # Pin on board connected to "neopixel"
num_pixels = 1         # Number of "neopixels"
pixel_brightness=0.3   # brightness 0-1, higher = brigther
led_scan_time = 0.5    # Time that the light stays on when card is scanned
SCAN_COLOR = BLUE      # What color to blink when card is scanned 

#Initialize neopixel object
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=pixel_brightness, auto_write=False)



##### RFID SETTINGS


RFID_PRE_PAD  = "__"          # If you want to pad the front of the ID, add it here
RFID_POST_PAD = ""          # if you want to pad the end of the ID, add it here
RFID_UPPERCASE_ID = True    # Do you want the ID writtend in uppercase letters ?
RFID_PRESS_ENTER  = True    # Do you want the keyboard to press enter after writing the ID

# RC522 PINS
miso = board.GP4
cs  = board.GP5
sck = board.GP6
mosi = board.GP7
rst = board.GP8


# Initalise RFID object
rfid = mfrc522.MFRC522(sck,mosi,miso, rst, cs)
rfid.set_antenna_gain(0x07 << 4)




################
#   INIT DONE  #
################


print("\n***** Scan your RFid tag/card *****\n")

prev_data = ""
prev_time = 0
timeout = 1



while True:

    (status, tag_type) = rfid.request(rfid.REQALL)

    if status == rfid.OK:
        (status, raw_uid) = rfid.anticoll()

        if status == rfid.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])

            if rfid_data != prev_data:
                pixels.fill(SCAN_COLOR)
                pixels.show()
                print(rfid_data)
                prev_data = rfid_data
                rfid_str = RFID_PRE_PAD + rfid_data + RFID_POST_PAD
                if RFID_UPPERCASE_ID:
                    rfid_str = rfid_str.upper()
                keyboard_layout.write(rfid_str)
                time.sleep(0.1)
                if RFID_PRESS_ENTER:
                    keyboard.send(Keycode.ENTER)
                time.sleep(1)
                pixels.fill(OFF)
                pixels.show()


            prev_time = time.monotonic()


    else:
        if time.monotonic() - prev_time > timeout:
            prev_data = ""
