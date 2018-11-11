#!/usr/bin/python
import os
import sys
from wallaby import *
from constants import *
from utilities import *
from driving import *
from actions import *


def main():

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


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
