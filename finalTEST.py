# Aidan Rafferty
# Phillips Hue Python FINAL Test Code before implementation
# Spring 2018

#!/usr/bin/python
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>BEGIN SETUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from phue import Bridge

import time
from neopixel import *
import argparse

#Import and setup for Photocells
import RPi.GPIO as GPIO, time, os
import numpy as np

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
b = Bridge('10.0.0.79')
#Connect to bridge
b.connect

print "\nBridge found...\n"
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
    #Create an array of photocell values
    photoVals = np.array([])
    sensor1 = RCtime(19)
    photoVals = np.append(photoVals, sensor1)
    sensor2 = RCtime(20)
    photoVals = np.append(photoVals, sensor2)
    sensor3 = RCtime(21)
    photoVals = np.append(photoVals, sensor3)
    sensor4 = RCtime(22)
    photoVals = np.append(photoVals, sensor4)
    sensor5 = RCtime(23)
    photoVals = np.append(photoVals, sensor5)
    sensor6 = RCtime(24)
    photoVals = np.append(photoVals, sensor6)
    sensor7 = RCtime(25)
    photoVals = np.append(photoVals, sensor7)
    sensor8 = RCtime(26)
    photoVals = np.append(photoVals, sensor8)

    #Compare photocell values to max value and trigger if they match
    if sensor1 == np.max(photoVals):
        #Blue lights
        print "SENSOR 1 ACTIVATED"
        #LED Activation
        colorWipe(strip, Color(0, 0, 255))
        #Hue Lights Activation
        lights = b.lights[0:4]
        for l in lights:
			#Change colors
		    l.xy = [0.1684, 0.0416]
		    l.hue = 47125
		    l.saturation = 253


    if sensor2 == np.max(photoVals):
        #Red Lights
        print "SENSOR 2 ACTIVATED"
        #LED Activation
        colorWipe(strip, Color(0, 255, 0))  # Red wipe
        #Hue Lights Activation
        b.set_group(1, 'on', True)
        lights = b.lights[0:4]
        for l in lights:
            #Change colors
            l.xy = [0.6099, 0.2867]
            l.hue = 63206
            l.saturation = 253

    if sensor3 == np.max(photoVals):
        #Green Lights
        print "SENSOR 3 ACTIVATED"
        #LED Activation
        colorWipe(strip, Color(100, 100, 100))
        #Hue Activation
        b.set_group(1, 'on', True)
        lights = b.lights[0:4]
        for l in lights:
            l.xy = [0.4084, 0.5168]
            l.hue = 25653
            l.saturation = 254

    if sensor4 == np.max(photoVals):
        #White Lights
        print "SENSOR 4 ACTIVATED"
        #LED Activation
        colorWipe(strip, Color(255, 255, 255))
        #Hue Activation
        b.set_group(1, 'on', True)
        lights = b.lights[0:4]
        for l in lights:
            l.xy = [0.457, 0.4098]
            l.hue = 14974
            l.saturation = 140

    if sensor5 == np.max(photoVals):
        #Summa Time Lights
        print "SENSOR 5 ACTIVATED"
        #LED Activation
        colorWipe(strip, Color(90, 190, 20))
        #Hue Activation
        b.set_group(1, 'on', True)
        l1 = b.lights[0]
		l2 = b.lights[1]
		l3 = b.lights[2]
		l4 = b.lights[3]

		l1.xy = [0.6134, 0.3674]
		l1.hue = 5933
		l1.saturation = 254

		l2.xy = [0.409, 0.518]
		l2.hue = 25599
		l2.saturation = 254

		l3.xy = [0.3225, 0.2767]
		l3.hue = 48089
		l3.saturation = 79

		l4.xy = [0.3471, 0.3957]
		l4.hue = 31101
		l4.saturation = 254



    if sensor6 == np.max(photoVals):
        #Red Rocks Sleepytime Lights
        print "SENSOR 6 ACTIVATED"
        #LED Activation
        colorWipe(strip, Color(10, 120, 80))
        #Hue Activation
        b.set_group(1, 'on', True)
        l1 = b.lights[0]
		l2 = b.lights[1]
		l3 = b.lights[2]
		l4 = b.lights[3]

		l1.xy = [0.5555, 0.3141]
		l1.hue = 63522
		l1.saturation = 186

		l2.xy = [0.6558, 0.3234]
		l2.hue = 65424
		l2.saturation = 240

		l3.xy = [0.6017, 0.3747]
		l3.hue = 6881
		l3.saturation = 252

		l4.xy = [0.6736, 0.3221]
		l4.hue = 65528
		l4.saturation = 253


    if sensor7 == np.max(photoVals):
        #Bitchin Lights
        print "SENSOR 7 ACTIVATED"
        #LED Activation
        colorWipe(strip, Color(10, 190, 20))
        #Hue Lights Activation
        b.set_group(1, 'on', True)
        l1 = b.lights[0]
		l2 = b.lights[1]
		l3 = b.lights[2]
		l4 = b.lights[3]

		l1.xy = [0.5641, 0.4024]
		l1.hue = 63206
		l1.saturation = 253

		l2.xy = [0.484, 0.2168]
		l2.hue = 58621
		l2.saturation = 253

		l3.xy = [0.6255, 0.3578]
		l3.hue = 4663
		l3.saturation = 253

		l4.xy = [0.1684, 0.0417]
		l4.hue = 47126
		l4.saturation = 253

    if sensor8 == np.max(photoVals):
        #Lights OFF
        print "SENSOR 8 ACTIVATED"
        #LED Activation
        colorWipe(strip, Color(0, 0, 0))
        #Hue Activation
        b.set_group(1, 'on', False)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>END LIGHT COMMANDS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


print('\nComplete!\n')
