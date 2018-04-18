# Aidan Rafferty
# Phillips Hue Python Test Code 2
# Spring 2018

#!/usr/bin/python
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>BEGIN SETUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from phue import Bridge

import time

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

while True:
	#Get command from users
	usercmd = raw_input("\nCommand: ")
	if usercmd == 'end':
		break
		print usercmd
	if usercmd == 'red':
		lights = b.lights[0:4]
		# Loop through given lights
		for l in lights:
			#Change colors
			l.xy = [0.6099, 0.2867]
			l.hue = 63206
			l.saturation = 253

			#Print light info
			# print("\n" + l.name)
			# print(l.xy)
			# print("Hue: {} ").format(l.hue)
			# print("Sat: {} ").format(l.saturation)
		print("\nLights set to RED")
	if usercmd == 'blue':
		#Get lights 0 through 4
		lights = b.lights[0:4]
		# Loop through given lights
		for l in lights:
			#Change colors
			l.xy = [0.1684, 0.0416]
			l.hue = 47125
			l.saturation = 253
		print("\nLights set to BLUE")


print('\nComplete!\n')
