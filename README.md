# PI PICO RFID READER WITH KEYBOARD OUTPUT

## About

This is the code, diagrams and STL's for a cheap pi pico based RFID reader that acts as a keyboard and types the cards UID

It uses a:
- Pi Pico (Running CircuitPython 7.x)
- RC522 RFID module
- WS2812 single "neopixel"  

there are some pictures of the final result in the images folder

## How to use

copy the contents of pico_code to a raspberry pi pico, running circuit-python 7, all libraries needed are included in the library folder 

***Note:*** The code assumes the keyboard layout being used is the standard icelandic layout, to change that just change the references in the "KEYBOARD SETTINGS" portion of main.py

***Notable variables to configure in main.py***

|Line nr | Variable   | note                                              |
|------- | ---------------- | ---------------------------------------------------------------- |
| 37     | pixel_brightness   | A value from 0 to 1, default is 0.3. Higher value = brighter led |
| 38     | led_scan_time      | How long the the light should stay on after being scanned (in seconds), default is 0.5 |
| 39     | SCAN_COLOR         | What color the led should display, color codes are defined in lines 24-29, default is BLUE |
| 49     | RFID_PRE_PAD       | Value to write before the card UID (1), default is no padding|
| 50     | RFID_POST_PAD      | Value to write after the card UID (1), default is no padding  |
| 51     | RFID_UPPERCASE_ID  | should the UID be written as uppercase letters ? default is True |
| 52     | RFID_PRESS_ENTER   | should the reader simulate enter being pressed after writing the UID ? default is True |



(1) output format is "${RFID_PRE_PAD}${RFID_UID}${RFID_POST_PAD}"
scanning a card with the value of "abc1234" with "RFID_UPPERCASE_ID" as True, RFID_PRE_PAD as "__" and RFID_POST_PAD as "--" returns "__ABC1234--" 


## Connection Diagram

![connection diagram](https://raw.githubusercontent.com/gbit-is/Pi-Pico-RFID-keyboard-reader/main/images/connection_diagram.png)

### Connecting RC522

I have seen more then one pin layout on RC5522 modules, don't trust the image, verify that you are connecting the correct pins according to this table


| Signal    | GPIO pi pico | Label on RC522 |
| --------- | ------------ | -------------- | 
| MISO      | GP.4         | "MISO"         | 
| CS        | GP.5         | "SDA or NSS"   |
| SCK       | GP.6         | "SCK"          |
| MOSI      | GP.7         | "MOSI"         |
| RST       | GP.8         | "RST"          |
| VCC       | 3.3V         | "VCC"          |
| GND       | GND          | "GND"          |

### Connecting the LED

I used a lilypad ws2812 "neopixel", mostly because I had one laying around. feel free to substitute this for any other single pixel "neopixel"
I think you can just cut a single one off a strip, but [single pixel products do exists](https://learn.adafruit.com/adafruit-neopixel-uberguide/individual-neopixels)
I hooked my LED up to GP.20 (pin 26)
