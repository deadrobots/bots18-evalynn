#!/usr/bin/python
import os
import sys
from wallaby import *


def drive(lspeed, rspeed, time=2000):
    motor(3, lspeed)
    motor(0, rspeed)
    msleep(time)


def waitForButton():
    ao()
    print('Press right button.')
    while right_button() == 0:
        pass
    print('Button pressed.')


def main():

    enable_servos()
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


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();