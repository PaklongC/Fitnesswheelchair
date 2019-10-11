#include <Arduino.h>
#include <SPI.h>
#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_SPI.h"
#include "Adafruit_BluefruitLE_UART.h"

#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BNO055.h>
#include <utility/imumaths.h>

#define BNO055_SAMPLERATE_DELAY_MS (200)
Adafruit_BNO055 bno = Adafruit_BNO055(55);

#include "BluefruitConfig.h"

#if SOFTWARE_SERIAL_AVAILABLE
#include <SoftwareSerial.h>
#endif



//all the pressure related stuff
#define PRESSURE_PIN A0
#define PRESSURE_PIN2 A1
#define PRESSURE_PIN3 A2

int prev_value_right  = -10000;
int prev_value_left   = -10000;
int prev_value_back   = -10000;

int value, prev_value = - 10000;
int value2, prev_value2 = - 10000;
int value3, prev_value3 = - 10000;

int deviation = 0;
int deviation2 = 0;
int deviation3 = 0;

double voltage_value, newton_value;
double voltage_value2, newton_value2;
double voltage_value3, newton_value3;

  int HIGH_left   = 0;
  int LOW_right   = 0;
  int LOW_left    = 0;
  int HIGH_right  = 0;


int used_voltage = 3;
boolean success;
bool calibration = false;

int testing = false;

bool test = false;

//pressure_sensing(int pressure_pin);

// Create the bluefruit object, either software serial...uncomment these lines
/*
  SoftwareSerial bluefruitSS = SoftwareSerial(BLUEFRUIT_SWUART_TXD_PIN, BLUEFRUIT_SWUART_RXD_PIN);

  Adafruit_BluefruitLE_UART ble(bluefruitSS, BLUEFRUIT_UART_MODE_PIN,
                      BLUEFRUIT_UART_CTS_PIN, BLUEFRUIT_UART_RTS_PIN);
*/

/* ...or hardware serial, which does not need the RTS/CTS pins. Uncomment this line */
// Adafruit_BluefruitLE_UART ble(BLUEFRUIT_HWSERIAL_NAME, BLUEFRUIT_UART_MODE_PIN);

/* ...hardware SPI, using SCK/MOSI/MISO hardware SPI pins and then user selected CS/IRQ/RST */
Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_CS, BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);

/* ...software SPI, using SCK/MOSI/MISO user-defined SPI pins and then user selected CS/IRQ/RST */
//Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_SCK, BLUEFRUIT_SPI_MISO,
//                             BLUEFRUIT_SPI_MOSI, BLUEFRUIT_SPI_CS,
//                             BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);


// A small helper
void error(const __FlashStringHelper*err) {
  Serial.println(err);
  while (1);
}

/* The service information */

int32_t imuServiceId;
int32_t orientationCharId;
/**************************************************************************/
/*!
    @brief  Sets up the HW an the BLE module (this function is called
            automatically on startup)
*/
/**************************************************************************/
//----------------------------------------------------------------------------------------SETUP STARTS HERE-------------------------------------------------------------------------------------------

void setup(void)
{
  while (!Serial); // required for Flora & Micro
  delay(500);


  Serial.begin(115200);
  setting_up_connection();
  
  //pressure sensing setup

  Serial.println("Setting up pressure sensing");
  pinMode(PRESSURE_PIN, INPUT); // setting pinmode to read analog value 
  pinMode(PRESSURE_PIN2, INPUT);
  pinMode(PRESSURE_PIN3, INPUT);
  pinMode(13, OUTPUT);
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);

/*
  deviation = 10;  // since there's a bit of a drift in the values if you put the same pressure over a certain period
                   // we ignore a divergence of around 1 percent around the previous value. 
  deviation2 = 10;
  deviation3 = 10;
  */
}


void send_pressure() {
 
  int right_pressure  = pressure_sensing(PRESSURE_PIN);
  int left_pressure   = pressure_sensing(PRESSURE_PIN3);
  int back_pressure   = pressure_sensing(PRESSURE_PIN2);

  prev_value_right  = right_pressure;
  prev_value_left   = left_pressure;
  prev_value_back   = back_pressure;

  if (test){
    int left_map = mapping_val(left_pressure, "LEFT");
    Serial.print(left_map);
    Serial.print("   ");

    int right_map = mapping_val(right_pressure, "RIGHT");
    Serial.println(right_map);
  }


  if (!test){
  // Command is sent when \n (\r) or println is called
  // AT+GATTCHAR=CharacteristicID,value
  ble.print( F("AT+GATTCHAR=") );
  ble.print( orientationCharId );
  ble.print( F(",") );
  ble.print(String(right_pressure));
  ble.print( F(",") );
  ble.print(String(back_pressure));
  ble.print( F(",") );
  ble.println(String(left_pressure));
  }
}

void Calibration(){
  Serial.println("Move your body to the left");
  delay(2000);
  HIGH_left   = analogRead(PRESSURE_PIN3);
  LOW_right   = analogRead(PRESSURE_PIN);

  if (test){
    Serial.print(HIGH_left + LOW_right);
    }

  Serial.println("Move your body to the right");
  delay(2000);
  LOW_left    = analogRead(PRESSURE_PIN3);
  HIGH_right  = analogRead(PRESSURE_PIN);

  if (test){
    Serial.print(LOW_left + HIGH_right);
    }

  Serial.println("Calibration complete!");
  delay(2000);
}




void loop(void) {

  if (test){
  if(calibration == false){
    Calibration();
    calibration = true;
  }}
  
  send_pressure();

  if (!test){
  // Check if command executed OK
    if ( !ble.waitForOK() ) {
//      error(F("Failed to get response!"));
      Serial.println("Failed to get response!");
      setting_up_connection();
    }
  }

  // Delay before next measurement update
  delay(200);  
}
