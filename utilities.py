#!/usr/bin/python
from wallaby import *


def init():
    camera_open_black()


def waitForButton():
    ao()
    print('Press right button.')
    while right_button() == 0:
        pass
    print('Button pressed.')
