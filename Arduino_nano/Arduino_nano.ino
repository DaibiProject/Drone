#include <SoftwareSerial.h>
#include "MSP.h"
#include <AES.h>
#include "./printf.h"
#include <SPI.h> 
#include <nRF24L01.h> 
#include <RF24.h> 
AES aes;
MSP msp;
SoftwareSerial mspSerial(1, 2);

void setup() {
  /* Initialisation du port série */
  Serial.begin(115200);
  ulSetup();
  delayMicroseconds(10);
  mspSetup();
  delayMicroseconds(10);
}

void loop() {
  ulSensor();
  mspCom();
  delayMicroseconds(10);
}
