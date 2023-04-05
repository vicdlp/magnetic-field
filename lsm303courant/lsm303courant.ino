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
  float Inormal[] = {0.0514, 0.078, 0.756};
  float Bnormal[] = {(compass.m.x) /11.0, (compass.m.y) /11.0 + 27, (compass.m.z) /9.8 - 78};
}

float Inormal[] = {0.0514, 0.078, 0.756};
float Bnormal[] = {(compass.m.x) /11.0, (compass.m.y) /11.0 + 27, (compass.m.z) /9.8 - 78};

void loop()
{
  compass.read();
  float B[] = {(compass.m.x) /11.0, (compass.m.y) /11.0 + 27, (compass.m.z) /9.8 - 78};
  float DB[] = {Bnormal[0]-B[0], Bnormal[1]-B[1], Bnormal[2]-B[2]};
  float DI[] = {DB[0]/51.988148768680326, DB[1]/67.49159802351841, DB[2]/41.66274632488274};
  float I[] = {Inormal[0]-DI[0], Inormal[1]-DI[1], Inormal[2]-DI[2]};
  String p1 = " ";
  Serial.println(I[0] + p1 + I[1] + p1 + I[2]);
  delay(100);
}
