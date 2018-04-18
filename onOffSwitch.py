# Aidan Rafferty
# Phillips Hue Python Test Code
# Spring 2018

#!/usr/bin/python

from phue import Bridge

#Library to beautify JSON data
import pprint
pp = pprint.PrettyPrinter(indent=4)
#Used this to fix a logging error from early on
import logging
logging.basicConfig()
#assign the bridge to value b
b = Bridge('10.0.0.79')
print "\nBridge found...\n"

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#FUNCTION
# Bool val if light is on or not (True for ON/ False for OFF)
bool1 = b.get_light(1, 'on')
bool2 = b.get_light(2, 'on')
bool3 = b.get_light(3, 'on')
bool4 = b.get_light(4, 'on')
# print "Light 1 is on: {}\n".format(bool1)

#Check to see what each lights status is
if(bool1 == True):
    print("Light 1 is ON")
else:
    print("Light 1 is OFF")

if(bool2 == True):
    print("Light 2 is ON")
else:
    print("Light 2 is OFF")

if(bool3 == True):
    print("Light 3 is ON")
else:
    print("Light 3 is OFF")

if(bool4 == True):
    print("Light 4 is ON")
else:
    print("Light 4 is OFF")

#Function that checks if light is on/off and changes to the opposite state
#Light 1
if(bool1 == False):
    b.set_light(1, 'on', True)
    print("\nLight 1 turned ON")
else:
    b.set_light(1, 'on', False)
    print("\nLight 1 turned OFF")
#Light 2
if(bool2 == False):
    b.set_light(2, 'on', True)
    print("Light 2 turned ON")
else:
    b.set_light(2, 'on', False)
    print("Light 2 turned OFF")
#Light 3
if(bool3 == False):
    b.set_light(3, 'on', True)
    print("Light 3 turned ON")
else:
    b.set_light(3, 'on', False)
    print("Light 3 turned OFF")
#Light 4
if(bool4 == False):
    b.set_light(4, 'on', True)
    print("Light 4 turned ON")
else:
    b.set_light(4, 'on', False)
    print("Light 4 turned OFF")
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

print('\nComplete!\n')
