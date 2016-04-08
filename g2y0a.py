#!/usr/bin/env python3

# simple class for a sharp g2y0a. goes great with the arduino sketch
# i've included wit this.

# i'd have used an a2d converter instead but i don't have any

import smbus

bus = smbus.SMBus(1)

class G2Y0A:
    """Sharp G2Y0A distance sensor. May work, may not. Who knows?"""
    __address = None

    def __init__(self, address):
        self.__address = address

    def get_distance(self):
        return bus.read_byte(self.__address)
