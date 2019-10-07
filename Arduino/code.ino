#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#define BNO055_SAMPLERATE_DELAY_MS (10)

Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);
double a, t;
double v, v0;

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
  v0=0;
  i=0;
  bno.setExtCrystalUse(true);

}

void loop(void)
{
  for(int i = 0;;i++)
  {
    imu::Vector<3> accelerometer = bno.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);
    t = BNO055_SAMPLERATE_DELAY_MS/1000.00;
    a = (accelerometer.x());

    v = v0 + a*t;
    v0 = v;

    Serial.print("Acceleration measured: ");
    Serial.println (a);
    Serial.print("Calculated speed: ");
    Serial.println(v);

    delay(BNO055_SAMPLERATE_DELAY_MS);
  }
}
