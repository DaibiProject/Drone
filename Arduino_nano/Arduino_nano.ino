#include <SoftwareSerial.h>
#include "MSP.h"
MSP msp;
SoftwareSerial mspSerial(7, 8);
/* Constantes pour les broches */
const byte TRIGGER_ULSF   = 5;  // Broche TRIGGER du capteur de distance de devant
const byte ECHO_ULSF      = 6;  // Broche ECHO du capteur de distance de devant

const byte TRIGGER_ULSL   = 9;  // Broche TRIGGER du capteur de distance de gauche
const byte ECHO_ULSL      = 10; // Broche ECHO du capteur de distance de gauche

const byte TRIGGER_ULSB   = 11; // Broche TRIGGER du capteur de distance de droite
const byte ECHO_ULSB      = 12; // Broche ECHO du capteur de distance de droite

const byte TRIGGER_ULSR   = 13; // Broche TRIGGER du capteur de distance de deriere
const byte ECHO_ULSR      = 14; // Broche ECHO du capteur de distance de deriere

/* Constantes pour le timeout */
const unsigned long MEASURE_TIMEOUT = 25000UL; // 25ms = ~8m à 340m/s

/* Vitesse du son dans l'air en mm/us */
const float SOUND_SPEED = 340.0 / 1000;

/* Niveaux de distance de 0 à 3 */
int LVL_FRONT; // Niveau de distance du capteur de devant
int LVL_LEFT;  // Niveau de distance du capteur de gauche
int LVL_BACK;  // Niveau de distance du capteur de derriere
int LVL_RIGHT; // Niveau de distance du capteur de droite

void setup() {
  /* Initialisation du port série */
  Serial.begin(115200);
  ulSetup();
  mspSetup();
}

void loop() {
  ulSensor();
}
