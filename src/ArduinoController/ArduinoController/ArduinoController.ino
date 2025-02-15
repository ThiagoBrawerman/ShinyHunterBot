#include <Arduino.h> // Arduino library
#include <math.h> // Math library
#include <NintendoSwitchControlLibrary.h> // Library for controller
#include <Wire.h> // I2C library

#define DELAY_MS 500 // delay in milliseconds
#define LED_PIN 13 // LED pin 13 for testing

char button = 0;
void setup() {

  // turn on controller
  pushButton(Button::B, DELAY_MS, 5); //turns on the controller by pressing B(any button works)

  // Join I2C bus as slave with address 8
  Wire.begin(0x8);

  // Call receiveEvent when data is received
  Wire.onReceive(receiveEvent);
  
  
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);
  delay(DELAY_MS*5);
  digitalWrite(LED_PIN, LOW); // Ready to use
  

}

void receiveEvent(int howMany) {
   

    // Read data from I2C bus
    while (Wire.available()) { // loop through all but the last
        button = Wire.read(); // receive byte as a character            
    }
 }

void loop() {
  switch (button){ 
          case 1:
            // Button A
            pushButton(Button::A,DELAY_MS,1);
            button = 0;
            break;

          case 2 :
            // Button X
            pushButton(Button::X, DELAY_MS,1);
            button = 0;
            break;

          case 3:
            // Button HOME
            pushButton(Button::HOME, DELAY_MS,1);
            button = 0;
            break;

          case 4:
            // DPad UP
            pushHat(Hat::UP, DELAY_MS,1);
            button = 0;
            break;

          default:
            button = 0;
            break;
        }
  delay(DELAY_MS/5);
  
  
}
