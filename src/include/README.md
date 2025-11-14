# GPIO Example Code
This repository contains the following files:
* test_gpio_directly.py
  * run using: `python3 test_gpio_directly.py`
  * expected behavior: an LED arrow should flash on the Raspberry Pi hat
  * this python script demonstrates how GPIO pins can be written to directly.
* hat_library.py
  * this is a library file that is not meant to be executed directly. Instead, other python scripts should import this script to use the library's fucntions.
  * this is a python library containing useful mappings of GPIO pins to logical objects such as Arrow, Motor, irSensor, and LinkedMotors. Using this library will make it much easier to program the robot to do things like turning arrows on/off or changing the speed of motors
* test_hat_library.py
  * run this using: `python3 test_hat_library.py`
  * this python script demonstrates how to use the hat_library.py to make motors move and arrows turn on/off
  * expected behavior: different arrows should flash on the robot, at the same time motors will move on the robot. Motor movement requires the AA battery pack to be connected to the Raspberry Pi hat.
* test_hat_library_sensor.py
  * run this using: `python3 test_hat_library_sensor.py`
  * this python script demonstrates how to use the hat_library.py to read the Digital Output values from Infrared Sensors
  * expected behavior: terminal should loop, printing values of IR sensor 1, IR sensor 2, then an example error of what happens
  when an invalid IR sensor pin is used.
