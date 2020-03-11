#include <SoftwareSerial.h>
#include "MSP.h"
#include <AES.h>
#include "./printf.h"
#include <SPI.h> 
#include <nRF24L01.h> 
#include <RF24.h> 
AES aes;
MSP msp;

// CAPTEURS ULTRASON
/* Constantes pour les broches */
const byte TRIGGER_ULSF   =   5;    // Broche TRIGGER du capteur de distance de devant
const byte ECHO_ULSF      =   6;    // Broche ECHO du capteur de distance de devant

const byte TRIGGER_ULSL   =   7;    // Broche TRIGGER du capteur de distance de gauche
const byte ECHO_ULSL      =   8;    // Broche ECHO du capteur de distance de gauche

const byte TRIGGER_ULSB   =   9;    // Broche TRIGGER du capteur de distance de droite
const byte ECHO_ULSB      =   10;   // Broche ECHO du capteur de distance de droite

const byte TRIGGER_ULSR   =   11;   // Broche TRIGGER du capteur de distance de deriere
const byte ECHO_ULSR      =   12;   // Broche ECHO du capteur de distance de deriere

const byte TRIGGER_ULSG   =   13;  // Broche TRIGGER du capteur de distance de dessous
const byte ECHO_ULSG      =   14;  // Broche ECHO du capteur de distance de dessous

/* Constantes pour le timeout */
const unsigned long MEASURE_TIMEOUT = 25000UL; // 25ms = ~8m à 340m/s

/* Vitesse du son dans l'air en mm/us */
const float SOUND_SPEED = 0.34;    // 340.0 / 1000

/* Niveaux de distance de 0 à 3 */
byte LVL_FRONT;                    // Niveau de distance du capteur de devant
byte LVL_LEFT;                     // Niveau de distance du capteur de gauche
byte LVL_BACK;                     // Niveau de distance du capteur de derriere
byte LVL_RIGHT;                    // Niveau de distance du capteur de droite
byte LVL_GROUND;                   // Niveau de distance du capteur du dessous

SoftwareSerial mspSerial(1, 2);

// AES
unsigned int keyLength [1] = {128};                                 // Taille de la clé 
byte *key = (unsigned char*)"DbItbDotw200";                         // Clé de cryptage
byte plain[] = "Open";                                              // Message a encrypter 
byte iv [N_BLOCK] ;
unsigned long long int myIv = 36753562;                             // Vecteur d'initialisation

// RADIO - NRF24L01
RF24 radio(13, 14);
const byte addresses[][6] = {"00001", "00002", "00003", "00004"};


void setup() {
  /* Initialisation du port série */
  Serial.begin(115200);
  ulSetup();
  delayMicroseconds(10);
  /* Initialisation liaison MSP */
  msp.begin(mspSerial);
  delayMicroseconds(10);
  /* Initialisation radio */
  radio.begin(); 
  radio.openWritingPipe(addresses[0]);                              // 00002 
  radio.openReadingPipe(1, addresses[1]);                           // 00001 
  radio.setPALevel(RF24_PA_MIN); 
  delayMicroseconds(10);
  /* Initialisation de printf pour l'AES */
  printf_begin();
  delayMicroseconds(10);
}

void loop() {
  ulSensor();
  mspCom();
  delayMicroseconds(10);
}
