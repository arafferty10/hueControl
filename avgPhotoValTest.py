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

        if sensor1 == np.max(photoVals):
            print "SENSOR 1 ACTIVATED"
        if sensor2 == np.max(photoVals):
            print "SENSOR 2 ACTIVATED"
        if sensor3 == np.max(photoVals):
            print "SENSOR 3 ACTIVATED"
        if sensor4 == np.max(photoVals):
            print "SENSOR 4 ACTIVATED"
        if sensor5 == np.max(photoVals):
            print "SENSOR 5 ACTIVATED"
        if sensor6 == np.max(photoVals):
            print "SENSOR 6 ACTIVATED"
        if sensor7 == np.max(photoVals):
            print "SENSOR 7 ACTIVATED"
        if sensor8 == np.max(photoVals):
            print "SENSOR 8 ACTIVATED"
        # print sensor1
        print photoVals
        print "Average Photocell Value = {}".format(np.mean(photoVals))
        print "Max Photocell Value = {}".format(np.max(photoVals))
        # print "Standard Deviation = {}\n".format(np.std(photoVals))
