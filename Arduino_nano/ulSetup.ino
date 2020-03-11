/* Constantes pour les broches */
const byte TRIGGER_ULSF   =   5;  // Broche TRIGGER du capteur de distance de devant
const byte ECHO_ULSF      =   6;  // Broche ECHO du capteur de distance de devant

const byte TRIGGER_ULSL   =   7;  // Broche TRIGGER du capteur de distance de gauche
const byte ECHO_ULSL      =   8; // Broche ECHO du capteur de distance de gauche

const byte TRIGGER_ULSB   =   9; // Broche TRIGGER du capteur de distance de droite
const byte ECHO_ULSB      =   10; // Broche ECHO du capteur de distance de droite

const byte TRIGGER_ULSR   =   11; // Broche TRIGGER du capteur de distance de deriere
const byte ECHO_ULSR      =   12; // Broche ECHO du capteur de distance de deriere

const byte TRIGGER_ULSG   =   13; // Broche TRIGGER du capteur de distance de dessous
const byte ECHO_ULSG      =   14; // Broche ECHO du capteur de distance de dessous

/* Constantes pour le timeout */
const unsigned long MEASURE_TIMEOUT = 25000UL; // 25ms = ~8m à 340m/s

/* Vitesse du son dans l'air en mm/us */
const float SOUND_SPEED = 340.0 / 1000;

/* Niveaux de distance de 0 à 3 */
byte LVL_FRONT;                    // Niveau de distance du capteur de devant
byte LVL_LEFT;                     // Niveau de distance du capteur de gauche
byte LVL_BACK;                     // Niveau de distance du capteur de derriere
byte LVL_RIGHT;                    // Niveau de distance du capteur de droite
byte LVL_GROUND;                   // Niveau de distance du capteur du dessous

void ulSetup() {
  /* Initialisation des broches */
  pinMode(TRIGGER_ULSF, OUTPUT);
  digitalWrite(TRIGGER_ULSF, LOW); // La broche TRIGGER doit être à LOW au repos
  pinMode(ECHO_ULSF, INPUT);
  pinMode(TRIGGER_ULSL, OUTPUT);
  digitalWrite(TRIGGER_ULSL, LOW);
  pinMode(ECHO_ULSL, INPUT);
  pinMode(TRIGGER_ULSB, OUTPUT);
  digitalWrite(TRIGGER_ULSB, LOW);
  pinMode(ECHO_ULSB, INPUT);
  pinMode(TRIGGER_ULSR, OUTPUT);
  digitalWrite(TRIGGER_ULSR, LOW);
  pinMode(ECHO_ULSR, INPUT);
  pinMode(TRIGGER_ULSG, OUTPUT);
  digitalWrite(TRIGGER_ULSG, LOW);
  pinMode(ECHO_ULSG, INPUT);
}
