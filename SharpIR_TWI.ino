/* Simple sketch for blasting out Sharp IR sensor readings over i2c
   by Will Oberndorfer
   
   Uses https://github.com/jeroendoggen/Arduino-distance-sensor-library
*/

#include <Wire.h>
#include <DistanceGP2Y0A21YK.h>

DistanceGP2Y0A21YK dist_sensor;

uint8_t distance;

void setup()
{
    Wire.begin(0x08);
    Wire.onRequest(requestEvent);
    dist_sensor.begin(A2);
}

void loop()
{
    delay(100);
    distance = dist_sensor.getDistanceCentimeter();
}


void requestEvent()
{
    Wire.write(distance);
}