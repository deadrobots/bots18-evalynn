#!/usr/bin/python
import os
import sys
from wallaby import *

# Good use of naming conventions for functions. Please use the same
# naming conventions for variables. lmotor should by lMotor, etc. 
# You have some constants defined, but you need to start using them.
# replace the "hard-coded" port numbers with your constants, and 
# define more constants for your sensor ports.
# I like the chuckDaCan action :) -LMB

lmotor = 3
rmotor = 0
claw = 0
arm = 3

def drive(lspeed, rspeed, time=2000):
    motor(3, lspeed) # Don't forget to use constants here -LMB
    motor(0, rspeed)
    msleep(time)


def waitForButton():
    ao()
    print('Press right button.')
    while right_button() == 0:
        pass
    print('Button pressed.')

def ChuckDaCan():
	# please use constants for all servo ports, and if you aren't using a constant for the
	# servo position value, then put a comment saying whether this moves the servo arm/claw up or down, or where... -LMB
    set_servo_position(0, 1400) 
    set_servo_position(3, 900)
    drive(100, 99, 2500)
    # Closes servo claw on can
    set_servo_position(0, 160)
    msleep(1000)
    set_servo_position(3, 2000)
    # Victory spin!
    drive(-100, 100, 5200)
    ao()
    waitForButton()
    # Chuck da can
    set_servo_position(0, 170)
    msleep(500)
    set_servo_position(3, 1400)
    msleep(200)
    set_servo_position(0, 1400)



def straightLineFollow(timeSecs):
    startTime = seconds()
    while (seconds() - startTime) < timeSecs:
        if analog(0) > 1000:
            drive(100, 100, 100)
        else:
            drive(100, 50, 100)


def lineFollow(timeSecs):
    startTime = seconds()
    while (seconds() - startTime) < timeSecs:
        if analog(0) > 1000: # Please also use constants for sensor ports, too! -LMB
            drive(100, 25, 50)
        else:
            drive(25, 100, 50)



def main():

    enable_servos()
    set_servo_position(0, 1400)
    set_servo_position(3, 900)
    msleep(500)
    # Line follows until near can
    while analog(1) < 2500:
        lineFollow(1)
    # Closes servo claw on can
    set_servo_position(0, 160)
    msleep(1000)
    set_servo_position(3, 2000)
    waitForButton()
    # Victory spin!
    drive(-100, 100, 5200)
    waitForButton()
    # Chuck da can
    set_servo_position(0, 170)
    msleep(500)
    set_servo_position(3, 1400)
    msleep(200)
    set_servo_position(0, 1400)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
