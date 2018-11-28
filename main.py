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
        ay = 0
        driveUntimed(100, 100)
        while ay < 250:
            ay = abs(accel_y())
            print(ay)
            msleep(50)
        drive(-50, -50, 1000)
        drive(0, 100, 1500)
        ao()
        msleep(1000)


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
