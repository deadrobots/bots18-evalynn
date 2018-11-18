#!/usr/bin/python
import os
import sys
from wallaby import *
from constants import *
from utilities import *
from driving import *
from actions import *


def main():
    driveUntimed(100, 100)
    ay = 0
    while ay < 250:
        ay = abs(accel_y())
        print(ay)
        msleep(50)
    print('I\'m done. Goodnight. Zzz')
    ao()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
