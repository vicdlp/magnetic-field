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
  float By = (compass.m.y) /11.0 + 27;
  float Bz = (compass.m.z) /9.8 - 78;
  String p1=" ";
  Serial.println(Bx + p1 + By + p1 + Bz);
//  Serial.print(t);
//  Serial.print(" ");
//  Serial.print(Bx);
//  Serial.print(" ");
//  Serial.print(By);
//  Serial.print(" ");
//  Serial.print(Bz);
//  Serial.print(" ");
//    aSerial.p(t).p(" ").p(Bx).p(" ").p(By).p(" ").pln(Bz);
    

}
