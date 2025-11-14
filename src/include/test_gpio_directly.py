#!/usr/bin/python

import time					# this allows us to use the sleep() function to tell our program to stop doing things for a while
import RPi.GPIO as GPIO 	# this allows us to use all the shortcuts provided by the RPi.GPIO library
GPIO.setmode(GPIO.BOARD)	# this configures the GPIO library to have the correct pin numbers
GPIO.setwarnings(False)		# this will supress any warnings that might get raised by the GPIO settings

pin=35						# this creates a variable called "pin" and sets the value of "pin" to 35
							# 35 is the pin connected to the arrow LEDs labeled LEFT. Changing this incorrectly could damage the rpi.

GPIO.setup(pin,GPIO.OUT)	# since the value of pin is 35, this line is the same as: GPIO.setup(35,GPIO.OUT)
							# this configures pin 35 to be an output pin, meaning we can set the voltage of the pin

# GPIO.setup(pin,GPIO.IN)	# this line begins with the '#' character, that means that when running the program,
							# this line will be skipped in later labs we will use GPIO.IN to configure pins to be 
							# input pins meaning we can read the voltage of the pin

try:						# this line allows the program to attempt to gracefully handle any unexpected situations
							# using this will allow us to execute the code in the "except" section at the bottom
							# of the program after the user enters ^c (ctrl + c)

	while True:				# while is a way of looping code "while" a statement is true. in this case, "True" is always true
							# so this section will loop forever

		# Loop starts at the new indentation level
		GPIO.output(pin, GPIO.LOW)	# this is setting the voltage on "pin" to LOW
		time.sleep(1)			# this causes the program to sleep for 1 second. nothing will happen during this time
		GPIO.output(pin, GPIO.HIGH)	# this is setting the voltage on "pin" to HIGH
		time.sleep(1)			# this causes the program to sleep for 1 second. nothing will happen during this time
	# Loop goes back to the start when the indenation level goes down

except KeyboardInterrupt:	# this section of code will run when a keyboard interrupt is detected, like ^c
	GPIO.cleanup()		# this will set all output GPIO pins to LOW before the program exits
