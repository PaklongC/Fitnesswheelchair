#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 bno = Adafruit_BNO055();

void setup(void)
{
  Serial.begin(9600);
  Serial.println("Accelerometer Raw Data Test"); Serial.println("");
  if(!bno.begin())
  {
    Serial.print("Ooops, no sensor detected ... Double check the wiring!");
    while(1);
  }
  delay(1000);
  bno.setExtCrystalUse(true);
}

void loop(void)
{
  imu::Vector<3> accelerometer = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  double a = double (accelerometer.x());
  Serial.println(a);
  delay(BNO055_SAMPLERATE_DELAY_MS);
}
