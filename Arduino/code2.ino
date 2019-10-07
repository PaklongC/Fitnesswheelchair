#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <math.h>
#define BNO055_SAMPLERATE_DELAY_MS (20)

const double r = 0.29;
double t, v;
int a, a2;

// Check I2C device address and correct line below (by default address is 0x29 or 0x28)
//                                    id, address
Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);

void setup(void)
{
  Serial.begin(9600);
  Serial.println("Orientation Sensor Test"); Serial.println("");

  /* Initialise the sensor */
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }

  delay(1000);

  bno.setExtCrystalUse(true);
}

void loop(void)
{
  /* Get a new sensor event */
  sensors_event_t event;
  bno.getEvent(&event);


  for (int i = 0;i<5;i++)
  {
    imu::Vector<3> orientation = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
    t = BNO055_SAMPLERATE_DELAY_MS/1000.00;
    float a = (orientation.x());
    delay(BNO055_SAMPLERATE_DELAY_MS);
    imu::Vector<3> orientation2 = bno.getVector(Adafruit_BNO055::VECTOR_EULER);
    float a2 = (orientation2.x());
    float delta_a = a2-a;

    float arc = 2*3.14*r*(delta_a/360);
    float v = arc/t;


    //Serial.print("Angle measured: ");
    //Serial.println (delta_a);
    Serial.print("Calculated speed: ");
    Serial.println(v);
  }

  /* Wait the specified delay before requesting nex data */
  delay(BNO055_SAMPLERATE_DELAY_MS);
}
