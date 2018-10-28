#!/usr/bin/python
from wallaby import *
from constants import *
from utilities import *
from driving import *


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
