#!/usr/bin/env python3

# test for G2Y0A class

import time
from g2y0a import G2Y0A

if __name__ == "__main__":
    sensor = G2Y0A(0x08)

    while True:
        print(sensor.get_distance())
        time.sleep(1)
