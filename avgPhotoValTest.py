#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os
import numpy as np

DEBUG = 1
GPIO.setmode(GPIO.BCM)

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

while True:
        photoVals = np.array([])
        sensor1 = RCtime(19)
        sensor2 = RCtime(19)
        sensor3 = RCtime(19)
        sensor4 = RCtime(19)
        sensor5 = RCtime(19)
        sensor6 = RCtime(19)
        sensor7 = RCtime(19)
        sensor8 = RCtime(19)
        # print sensor1
        photoVals = np.append(photoVals, sensor1, sensor2, sensor3, sensor4, sensor5, sensor6, sensor7, sensor8)
        print photoVals
