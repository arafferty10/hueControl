# Aidan Rafferty
# Phillips Hue Python FINAL Code for Inclass Demonstration
# Spring 2018

#!/usr/bin/python
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>BEGIN SETUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
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

print "\nBeginning...\n"

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
        print "\nSENSOR 1 ACTIVATED"
        print "BLUE"
        #LED Activation
        colorWipe(strip, Color(0, 0, 255))


    if sensor2 == np.max(photoVals):
        #Red Lights
        print "\nSENSOR 2 ACTIVATED"
        print "RED"
        #LED Activation
        colorWipe(strip, Color(0, 255, 0))  # Red wipe

    if sensor3 == np.max(photoVals):
        #Green Lights
        print "\nSENSOR 3 ACTIVATED"
        print "GREEN"
        #LED Activation
        colorWipe(strip, Color(255, 0, 0))


    if sensor4 == np.max(photoVals):
        #White Lights
        print "\nSENSOR 4 ACTIVATED"
        print "WHITE"
        #LED Activation
        colorWipe(strip, Color(255, 255, 255))


    if sensor5 == np.max(photoVals):
        #Summa Time Lights
        print "\nSENSOR 5 ACTIVATED"
        print "SUMMA TIME"
        #LED Activation
        colorWipe(strip, Color(90, 190, 20))


    if sensor6 == np.max(photoVals):
        #Red Rocks Sleepytime Lights
        print "\nSENSOR 6 ACTIVATED"
        print "RED ROCKS SLEEPY"
        #LED Activation
        colorWipe(strip, Color(10, 120, 80))


    if sensor7 == np.max(photoVals):
        #Bitchin Lights
        print "\nSENSOR 7 ACTIVATED"
        print "BITCHIN"
        #LED Activation
        colorWipe(strip, Color(10, 190, 20))

    if sensor8 == np.max(photoVals):
        #Lights OFF
        print "\nSENSOR 8 ACTIVATED"
        print "OFF"
        #LED Activation
        colorWipe(strip, Color(0, 0, 0))


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>END LIGHT COMMANDS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


print('\nComplete!\n')
