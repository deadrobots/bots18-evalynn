#!/usr/bin/python
from wallaby import *
from constants import *
from utilities import *
from driving import *
import random as r


def squigglyLineFollowGrabCan():
    enable_servos()
    set_servo_position(claw, 1400)
    set_servo_position(arm, 900)
    msleep(500)
    # Line follows until near can
    print(analog(ET))
    while analog(ET) < 2950:
        lineFollow(.1)
        print(analog(ET))
    print(analog(ET))
    waitForButton()
    # Closes servo claw on can
    drive(25, 25, 2500)
    set_servo_position(claw, 60)
    msleep(1000)
    set_servo_position(arm, 2000)
    waitForButton()
    # Victory spin!
    drive(-100, 100, 5200)
    waitForButton()
    # Chuck da can
    set_servo_position(claw, 170)
    msleep(500)
    set_servo_position(arm, 1400)
    msleep(200)
    set_servo_position(claw, 1400)


def chuckDaCan():
    # If you aren't using a constant for the servo position value, then put a comment saying whether this moves the
    # servo arm/claw up or down, or where... -LMB
    set_servo_position(claw, 1400)
    set_servo_position(arm, 900)
    drive(100, 99, 2500)
    # Closes servo claw on can
    set_servo_position(claw, 160)
    msleep(1000)
    set_servo_position(arm, 2000)
    # Careful. There's no sleep after this call to set_servo_position(). The servo will be trying
    # to move while your wheels are driving. This can cause unexpected things to happen - LMB
    # Victory spin!
    drive(-100, 100, 5200)
    ao()
    waitForButton()
    # Chuck da can
    set_servo_position(claw, 170)
    msleep(500)
    set_servo_position(arm, 1400)
    msleep(200)
    set_servo_position(claw, 1400)
    # Don't forget to add a sleep call here. This last call to set_servo_position() may behave unexpectedly without
    # it -LMB

"""
Your code is very concise here. Well done. It doesn't have to be super complicated to make
a cool robot. 
A challenge for you, if you're up for it: remove the msleep() from inside your loop, and check
the gyrometer more frequently. Then make an average of the last five gyro readings, so that your
robot will be less sensitive to small bumps, and only sensitive to large bumps. (This has a 
different effect than simply changing the gyro threshold). 
To do this, use lists:
myGyroList = [] # new list
myGyroList.append(gyro_y()) # adds a number to the "top" your list
myGyroList.pop(0) # removes the oldest value, aka the number on the "bottom" of the list
then use a for: loop to take the average over all five list values.
-LMB
"""
def zuZuBot():
    while True:
        ay = 0
        n = r.randint(500, 2001)
        driveUntimed(100, 100)
        while ay < 250:
            ay = abs(accel_y())
            print(ay)
            msleep(50)
        drive(-50, -50, 1500)
        drive(0, 100, n)
        ao()
        msleep(1000)
