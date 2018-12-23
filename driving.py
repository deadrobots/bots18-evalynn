#!/usr/bin/python
from wallaby import *
from constants import *
from utilities import *


def drive(lSpeed, rSpeed, time=2000):  # Straight Value = (97, 100)
    motor(lMotor, lSpeed)
    motor(rMotor, rSpeed)
    msleep(time)


def driveUntimed(lSpeed, rSpeed):
    motor(lMotor, lSpeed)
    motor(rMotor, rSpeed)


def driveFreeze(lSpeed, rSpeed, time=2000):
    motor(lMotor, lSpeed)
    motor(rMotor, rSpeed)
    msleep(time)
    ao()
    freeze(lMotor)
    freeze(rMotor)
    msleep(500)


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
            motor(lMotor, 50)
            motor(rMotor, 5)
        else:
            motor(lMotor, 5)
            motor(rMotor, 50)
