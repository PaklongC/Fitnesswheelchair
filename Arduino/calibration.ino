#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#define BNO055_SAMPLERATE_DELAY_MS (100)

Adafruit_BNO055 myIMU = Adafruit_BNO055();

void setup()
{
  Serial.begin(115200);
  myIMU.begin();

  Serial.println("Kalibratie van de BNO055 gemaakt door groep 4");
  Serial.println();
  Serial.println("Cijfers (in volgorde): versnelling in x, y en z-richting");
  Serial.println("Kalibratieconstantes: 0 = slecht, 3 = volledig gekalibreerd");
  Serial.println("Volgorde van constantes: acceleratie, gyroscope, magnetometer en het systeem");
  // Kalibratie: Gyro = stilhouden, Magneto = rondswingen en Accelerometer = in elke axis even stilhouden.
  delay(2000);

  int8_t temp=myIMU.getTemp();
  myIMU.setExtCrystalUse(true);
  Serial.println();
}

void loop()
{
  uint8_t system, gyro, accel, mg  =0;
  myIMU.getCalibration(&system, &gyro, &accel, &mg);
  imu::Vector<3> acc =myIMU.getVector(Adafruit_BNO055::VECTOR_ACCELEROMETER);

  Serial.print(acc.x());
  Serial.print(", ");
  Serial.print(acc.y());
  Serial.print(", ");
  Serial.print(acc.z());
  Serial.print(", ");
  Serial.print(accel);
  Serial.print(", ");
  Serial.print(gyro);
  Serial.print(", ");
  Serial.print(mg);
  Serial.print(", ");
  Serial.println(system);
}
