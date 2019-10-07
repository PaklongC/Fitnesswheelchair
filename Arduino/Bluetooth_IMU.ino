#include <Arduino.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>
#include <math.h>
#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_SPI.h"
#include "Adafruit_BluefruitLE_UART.h"

#include "BluefruitConfig.h"

#if SOFTWARE_SERIAL_AVAILABLE
  #include <SoftwareSerial.h>
#endif

#include "BluefruitConfig.h"


#define LED_PIN2

Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_CS, BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);


#define BNO055_SAMPLERATE_DELAY_MS (20)

const double r = 0.29;
double t, v;
int a, a2;

// GATT service information
int32_t imuServiceId;
int32_t rotationCharId;
int32_t orientationCharId;

// Check I2C device address and correct line below (by default address is 0x29 or 0x28)
//                                    id, address
Adafruit_BNO055 bno = Adafruit_BNO055(-1, 0x28);

//---------------------------------------------------------------------------------------

// A small helper
void error(const __FlashStringHelper*err) {
  if (Serial.available()) {
    Serial.println(err);
  }
}

//---------------------------------------------------------------------------------------

void setup(void){
  delay(500);
  boolean success;

  Serial.begin(115200);

  // Initialise the module
  if ( !ble.begin(VERBOSE_MODE) ) {
    error(F("Couldn't find Bluefruit, make sure it's in CoMmanD mode & check wiring."));
  }

  /* Initialise the sensor */
  if(!bno.begin())
  {
    /* There was a problem detecting the BNO055 ... check your connections */
    Serial.print("Ooops, no BNO055 detected ... Check your wiring or I2C ADDR!");
    while(1);
  }
  delay(1000);
  bno.setExtCrystalUse(true);

  if (! ble.factoryReset() ){
       error(F("Couldn't factory reset."));
  }

  // Disable command echo from Bluefruit
  ble.echo(false);

  // Print Bluefruit information
  ble.info();
  ble.verbose(true);

  // Change the device name to fit its purpose
  if (! ble.sendCommandCheckOK(F("AT+GAPDEVNAME=Noisy Left Wheel")) ) {
    error(F("Could not set device name."));
  }

/* Add the IMU Service definition
  success = ble.sendCommandWithIntReply( F("AT+GATTADDSERVICE=UUID128=00-11-00-11-44-55-66-77-88-99-AA-BB-CC-DD-EE-FF"), &imuServiceId);
  if (! success) {
    error(F("Could not add Orientation service."));
  }
*/
    // Add the Orientation characteristic
  success = ble.sendCommandWithIntReply( F("AT+GATTADDCHAR=UUID128=02-11-88-33-44-55-66-77-88-99-AA-BB-CC-DD-EE-FG,PROPERTIES=0x10,MIN_LEN=1,MAX_LEN=17,VALUE=\"\""), &orientationCharId);
  if (! success) {
    error(F("Could not add Orientation characteristic."));
  }

  // Add the Orientation Service to the advertising data
  // (needed for Nordic apps to detect the service)
  ble.sendCommandCheckOK( F("AT+GAPSETADVDATA=02-01-06-05-02-0d-18-0a-18") );

  // Reset the device for the new service setting changes to take effect
  ble.reset();
}

void velocity(){
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

    ble.print( F("AT+GATTCHAR=") );
    ble.println( orientationCharId );
    ble.print( "calculated speed" );
    ble.println(v);
  }
}

void loop(void) {
  velocity();
  // Check if command executed OK
  if ( !ble.waitForOK() ) {
    error(F("Failed to get response!"));
  }

  delay(BNO055_SAMPLERATE_DELAY_MS);
}
