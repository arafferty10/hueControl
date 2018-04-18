# Aidan Rafferty
# Phillips Hue Python Test Code
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
# b.connect()

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>END OF SETUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Get the bridge state (This returns the full dictionary that you can explore)
# pp.pprint(b.get_api())

# You can also control multiple lamps by sending a list as lamp_id
# b.set_light( [1,2,3,4], 'on', True)

# Turn group 1 off
b.set_group(1, 'on', True)

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Get lights 0 through 4
lights = b.lights[0:4]

# Print light names and color values
for l in lights:
    print(l.name)
    l.xy = [random.random(),random.random()]
    print(l.xy)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

#>>>>>>>>>>>Random colored lights>>>>>>>>>>>>>>>>>>>>
# lights = b.get_light_objects()
# lights = b.get_light([1,2,3,4])
#
# for light in lights:
# 	light.brightness = 254
# 	light.xy = [random.random(),random.random()]

# Get a dictionary with the light name as the key
# light_names = b.get_light_objects('name')
#
# # Set lights using name as key
# for light in ["Bedroom"]
#     light_names[light].on = True
#     light_names[light].hue = 15000
#     light_names[light].saturation = 120

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# Get the name of a lamp
# print b.get_light(1, 'name')

# #Turn on light 1
# b.set_light([1,2,3,4], 'on', True)

# Set brightness of lamp 1 to max
# b.set_light(1, 'bri', 254)

# List groups
# b.get_group()

# List group 1
# gp1List = b.get_group(1)
# pp.pprint(gp1List)

# Get name of group 1
# group1 = b.get_group(1, 'name')
# print "Group 1 is called: {}".format(group1)

print('\nComplete!\n')
