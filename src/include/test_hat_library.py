#!/usr/bin/python

import hat_library as hatLib    # import all functions, objects, and contents of hat_library.py and use the 
                                # nickname "hatLib" to access them
import time			# this allows us to use the sleep() function to tell our program to stop doing things for a while
import RPi.GPIO as GPIO 	# import all functions, objects, and contents of the RPi.GPIO installed python library and use the
                                # nickname "GPIO" to access them

# Create "Motor" objects to allow us to interact with individual motors instead of GPIO pins 
motor_1 = hatLib.Motor("MOTOR1", 1)
motor_2 = hatLib.Motor("MOTOR2", 1)
motor_3 = hatLib.Motor("MOTOR3", 1)
motor_4 = hatLib.Motor("MOTOR4", 1)

# Create a "LinkedMotors" object to allow us to drive all motors at once, if desired
motorAll = hatLib.LinkedMotors(motor_1, motor_2, motor_3, motor_4)

# Create "Arrow" objects to allow us to interact with individual LED arrows instead of GPIO pins 
arrow_back = hatLib.Arrow(1)
arrow_left = hatLib.Arrow(2)
arrow_front = hatLib.Arrow(3) 
arrow_right = hatLib.Arrow(4)

# This segment drives the motors in the direction listed below:
# forward and reverse takes speed in percentage(0-100)

try:
    while True:
#-----------To Drive the Motors Forward------------# 
        print("Robot Moving Forward")
        arrow_front.on()                # "Arrow" objects have member functions to turn themselves "on" or "off"
        arrow_back.off()
        arrow_left.off()
        arrow_right.off()
        motorAll.forward(100)           # "LinkedMotors" objects have member functions to move all linked motors: 
                                        # "forward", "reverse", or "stop"
        time.sleep(2)
#--------------------------------------------------#

#-----------To Drive the Motors backwards------------# 
        print("Robot Moving Backward")
        arrow_front.off()
        arrow_back.on()
        arrow_left.off()
        arrow_right.off()
        motorAll.reverse(100)
        time.sleep(2)
#--------------------------------------------------#

#-----------To Drive the Motors Left---------------#
        print("Robot Moving Left")
        arrow_front.off()
        arrow_back.off()
        arrow_left.on()
        arrow_right.off()
        motor_1.stop()                  # "Motor" objects have member functions to move the motor "forward", "reverse", or "stop"
        motor_2.stop()
        motor_3.forward(100)
        motor_4.forward(100)
        time.sleep(2)
#--------------------------------------------------#

#----------To Drive the Motors Right---------------#
        print("Robot Moving Right")
        arrow_front.off()
        arrow_back.off()
        arrow_left.off()
        arrow_right.on()
        motor_1.forward(100)
        motor_2.forward(100)
        motor_3.stop()
        motor_4.stop()
        time.sleep(2)
#-------------------------------------------------#

#---------To Stop the Motors----------------------#
        print("Robot Stop")
        arrow_front.off()
        arrow_back.off()
        arrow_left.off()
        arrow_right.off()
        motorAll.stop()
        time.sleep(5)
#-------------------------------------------------#

        
except KeyboardInterrupt:
    GPIO.cleanup()

    
