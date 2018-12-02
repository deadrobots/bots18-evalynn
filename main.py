#!/usr/bin/python
import os
import sys
from wallaby import *
from constants import *
from utilities import *
from driving import *
from actions import *


def main():
    while True:
        driveUntimed(100, 0)
        ay = abs(accel_y())
        print(ay)
        msleep(50)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
