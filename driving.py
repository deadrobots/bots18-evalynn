#!/usr/bin/python
from wallaby import *
from constants import *
from utilities import *


def drive(lSpeed, rSpeed, time=2000):
    motor(lMotor, lSpeed)
    motor(rMotor, rSpeed)
    msleep(time)


# Line follow but does not work well on curved lines
def straightLineFollow(timeSecs):
    startTime = seconds()
    while (seconds() - startTime) < timeSecs:
        if analog(topHat) > 1000:
            drive(100, 100, 100)
        else:
            drive(100, 50, 100)


def lineFollow(timeSecs):
    startTime = seconds()
    while (seconds() - startTime) < timeSecs:
        if analog(topHat) > 1000:
            motor(lMotor, 100)
            motor(rMotor, 10)
        else:
            motor(lMotor, 10)
            motor(rMotor, 100)
