# Aidan Rafferty
# Phillips Hue Python Test Code 2
# Spring 2018

#!/usr/bin/python
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>BEGIN SETUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# from phue import Bridge

import time
from neopixel import *
import argparse

#Import and setup for Photocells
import RPi.GPIO as GPIO, time, os

DEBUG = 1
GPIO.setmode(GPIO.BCM)

#Library to beautify JSON data
import pprint
pp = pprint.PrettyPrinter(indent=4)
#Used this to fix a logging error from early on
import logging
logging.basicConfig()
#Random Library
import random
#assign the bridge to value b
# b = Bridge('10.0.0.79')
#
# b.connect

# print "\nBridge found...\n"
print "\nBeginning Test...\n"

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
# b.connect()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>END OF SETUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Turn group 1 on
# b.set_group(1, 'on', True)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>PHOTOCELL SERIAL READ CODE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>END PHOTOCELL SERIAL READ >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>LED FUNCTIONS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
    """Movie theater light style chaser animation."""
    for j in range(iterations):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, color)
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainbow(strip, wait_ms=20, iterations=1):
    """Draw rainbow that fades across all pixels at once."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((i+j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256*iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel((int(i * 256 / strip.numPixels()) + j) & 255))
        strip.show()
        time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
    """Rainbow movie theater light style chaser animation."""
    for j in range(256):
        for q in range(3):
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, wheel((i+j) % 255))
            strip.show()
            time.sleep(wait_ms/1000.0)
            for i in range(0, strip.numPixels(), 3):
                strip.setPixelColor(i+q, 0)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>END LED FUNCTIONS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
strip.begin()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>LIGHT COMMANDS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
while True:
    # print RCtime(19)

    if RCtime(19) > RCtime(20) and RCtime(21) and RCtime(22) and RCtime(23) and RCtime(24) and RCtime(25) and RCtime(26):
        colorWipe(strip, Color(0, 0, 255))

    if RCtime(20) > RCtime(19) and RCtime(21) and RCtime(22) and RCtime(23) and RCtime(24) and RCtime(25) and RCtime(26):
        colorWipe(strip, Color(0, 255, 0))  # Red wipe

    if RCtime(21) > RCtime(19) and RCtime(20) and RCtime(22) and RCtime(23) and RCtime(24) and RCtime(25) and RCtime(26):
        colorWipe(strip, Color(100, 100, 100))

    if RCtime(22) > RCtime(19) and RCtime(20) and RCtime(21) and RCtime(23) and RCtime(24) and RCtime(25) and RCtime(26):
        colorWipe(strip, Color(50, 155, 200))

    if RCtime(23) > RCtime(19) and RCtime(20) and RCtime(21) and RCtime(22) and RCtime(24) and RCtime(25) and RCtime(26):
        colorWipe(strip, Color(200, 55, 100))

    if RCtime(24) > RCtime(19) and RCtime(20) and RCtime(21) and RCtime(22) and RCtime(23) and RCtime(25) and RCtime(26):
        colorWipe(strip, Color(150, 20, 160))

    if RCtime(25) > RCtime(19) and RCtime(20) and RCtime(21) and RCtime(22) and RCtime(23) and RCtime(24) and RCtime(26):
        colorWipe(strip, Color(10, 190, 20))

    if RCtime(26) > RCtime(19) and RCtime(20) and RCtime(21) and RCtime(22) and RCtime(23) and RCtime(24) and RCtime(25):
        colorWipe(strip, Color(75, 90, 40))

    print "Sensor 1: {}".format(RCtime(19))   # Read RC timing using pin #18
    print "Sensor 2: {}".format(RCtime(20))
    print "Sensor 3: {}".format(RCtime(21))
    print "Sensor 4: {}".format(RCtime(22))
    print "Sensor 5: {}".format(RCtime(23))   # Read RC timing using pin #18
    print "Sensor 6: {}".format(RCtime(24))
    print "Sensor 7: {}".format(RCtime(25))
    print "Sensor 8: {}\n".format(RCtime(26))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>END LIGHT COMMANDS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


print('\nComplete!\n')
