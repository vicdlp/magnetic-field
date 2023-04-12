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
  compass.read();
  
}

  float Inormal[] = {0.0514, 0.078, 0.756};
  float Bnormal[] = {-27, -37, -33};

void loop()
{
  compass.read();
  float B[] = {(compass.m.x) /11.0, (compass.m.y) /11.0 + 27, (compass.m.z) /9.8 - 78};
  float DB[] = {Bnormal[0]-B[0], Bnormal[1]-B[1], Bnormal[2]-B[2]};
  float DI[] = {DB[0]*0.02, DB[1]*0.014, DB[2]*0.024};
  float I[] = {Inormal[0]-DI[0], Inormal[1]-DI[1], Inormal[2]-DI[2]};
  String p1 = " ";
  Serial.println(I[0] + p1 + I[1] + p1 + I[2]);
  Serial.println(B[0] + p1 + B[1] + p1 + B[2]);
  delay(100);
}
