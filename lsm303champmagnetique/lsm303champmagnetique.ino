#include <Wire.h>
#include <LSM303.h>
#include <advancedSerial.h>

LSM303 compass;

void setup()
{
  
  Serial.begin(2000000);
  aSerial.setPrinter(Serial);
  Wire.begin();
  compass.init();
  compass.enableDefault();
}

void loop()
{
  compass.read();
  float Bx = (compass.m.x) /11.0;
  float By = (compass.m.y) /11.0;
  float Bz = (compass.m.z) /9.8;
  String p1=" ";
  Serial.println(Bx + p1 + By + p1 + Bz);

}
