#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 bno = Adafruit_BNO055();
unsigned long t0,t1,t2;
double a, a1, v;

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
  t0=0;
}

void loop(void)
{
  imu::Vector<3> accelerometer = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
  a = double (accelerometer.x());
  t2 = 1000*millis();  //take current time
  t1 = t2 - t0;    // td = time since last update
  t0 = t2;        //set last time to current time
  v = v + a1*t1; //increase or decrease speed
  a1 = a;          //set new acceleration;

  Serial.print("Time elapsed: ");
  Serial.println (t1);
  Serial.print("Acceleration measured: ");
  Serial.println (a);
  Serial.print("Calculated speed: ");
  Serial.println(v);
  delay(BNO055_SAMPLERATE_DELAY_MS);
  delay(3000);
}
}
