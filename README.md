Simple Sharp TWI thing
======================

Uses [https://github.com/jeroendoggen/Arduino-distance-sensor-library](this Arduino sensor library) and Wire to make a simple i2c slave interface for a Sharp GP2Y0A21YK sensor.

Included is a Python example script for Raspberry Pi that will read from the sensor once per second.

Instructions
------------

Install the library by cloning it and adding the DistanceSensor directory in the library manager in arduino

Shove the pins for the sensor into 5V, ground, and pin A2 on the arduino.

Connect SCL and SDA between the arduino and the pi. You may need to pull them high.

Put the two python scripts onto the pi and run them.

Will it work? Who knows! I haven't tested it yet. glhf
