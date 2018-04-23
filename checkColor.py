# Aidan Rafferty
# Phillips Hue Python Test Code 2
# Spring 2018

#!/usr/bin/python
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>BEGIN SETUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from phue import Bridge

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
print "\nBridge found...\n"

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
b.connect()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>END OF SETUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Turn group 1 on
b.set_group(1, 'on', True)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> 
#Set lights to variables
l1 = b.lights[0]
l2 = b.lights[1]
l3 = b.lights[2]
l4 = b.lights[3]

#Change colors
# l1.xy = [0.6099, 0.2867]
# l1.hue = 63206
# l1.saturation = 253

#Print light info
print(l1.name)
print(l1.xy)
print("Hue: {} ").format(l1.hue)
print("Sat: {} ").format(l1.saturation)

print("\n" + l2.name)
print(l2.xy)
print("Hue: {} ").format(l2.hue)
print("Sat: {} ").format(l2.saturation)

print("\n" + l3.name)
print(l3.xy)
print("Hue: {} ").format(l3.hue)
print("Sat: {} ").format(l3.saturation)

print("\n" + l4.name)
print(l4.xy)
print("Hue: {} ").format(l4.hue)
print("Sat: {} ").format(l4.saturation)

print('\nComplete!\n')
