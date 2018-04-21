# Aidan Rafferty
# Phillips Hue Python Test Code 2
# Spring 2018

#!/usr/bin/python
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>BEGIN SETUP>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
from phue import Bridge

#Dependancies for LEDs
import time
from neopixel import *
import argparse

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

	if usercmd == 'green':
		lights = b.lights[0:4]
		for l in lights:
			l.xy = [0.4084, 0.5168]
			l.hue = 25653
			l.saturation = 254
		print("\nLights set to GREEN")
	if usercmd == 'bitchin':
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
		print("\nLights set to BITCHIN")


print('\nComplete!\n')
