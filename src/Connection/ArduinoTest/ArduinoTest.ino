#include <Arduino.h> // Arduino library
#include <Wire.h> // I2C library

// LED pin 13
#define LED_PIN 13

void setup() {
    // Join I2C bus as slave with address 8
    Wire.begin(0x8);

    // Call receiveEvent when data is received
    Wire.onReceive(receiveEvent);

    // Set LED pin as output and turn it off
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);
}

void receiveEvent(int howMany) {
    // Read data from I2C bus
    while (Wire.available()) { // loop through all but the last
        char c = Wire.read(); // receive byte as a character
        digitalWrite(LED_PIN, c);
    }
 }

void blinkLED (int pin){
    delay(1000);
    digitalWrite(pin, LOW);
    delay(1000);
    digitalWrite(pin, HIGH);
  
}

void loop() {
    //blinkLED(LED_PIN);
    delay(100);
}
