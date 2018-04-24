#!/usr/bin/env python

# Example for RC timing reading for Raspberry Pi
# Must be used with GPIO 0.3.1a or later - earlier verions
# are not fast enough!

import RPi.GPIO as GPIO, time, os

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
        print "Sensor 1: {}".format(RCtime(19))   # Read RC timing using pin #18
        print "Sensor 2: {}".format(RCtime(20))
        print "Sensor 3: {}".format(RCtime(21))
        print "Sensor 4: {}".format(RCtime(22))
        print "Sensor 5: {}".format(RCtime(23))   # Read RC timing using pin #18
        print "Sensor 6: {}".format(RCtime(24))
        print "Sensor 7: {}".format(RCtime(25))
        print "Sensor 8: {}\n".format(RCtime(26))
