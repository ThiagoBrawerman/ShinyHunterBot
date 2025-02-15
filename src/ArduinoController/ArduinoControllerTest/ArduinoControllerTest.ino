#include <Arduino.h>
#include <math.h>
#include <NintendoSwitchControlLibrary.h>


#define DELAY_MS 500
#define LED_PIN 13

void setup() {
  // put your setup code here, to run once:
  
  pushButton(Button::B, 500, 5); //turns on the controller by pressing B(any button works)
  pinMode(LED_PIN, OUTPUT);

}

void loop() {

  // test LED
  digitalWrite(LED_PIN, HIGH);
  
  // test controller functionality

  //Enter the game
  pushButton(Button::A, DELAY_MS, 2);
  delay(DELAY_MS);

  //Exit the game
  pushButton(Button::HOME, DELAY_MS, 1);
  delay(5*DELAY_MS);

  //Close the game
  pushButton(Button::X, DELAY_MS, 1);
  pushButton(Button::A, DELAY_MS, 1);

  digitalWrite(LED_PIN, LOW);

  delay(5*DELAY_MS);

  
}
