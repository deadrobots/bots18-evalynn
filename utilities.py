#!/usr/bin/python
import os
import sys
from wallaby import *

def waitForButton():
    ao()
    print('Press right button.')
    while right_button() == 0:
        pass
    print('Button pressed.')
