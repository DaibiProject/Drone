RF24 radio(13, 14);
const byte addresses[][6] = {"00001", "00002", "00003", "00004"};
unsigned int keyLength [1] = {128};                                 // Taille de la clé 
byte *key = (unsigned char*)"DbItbDotw200";                         // Clé de cryptage
byte plain[] = "Open";                                              // Message a encrypter 
byte iv [N_BLOCK] ;
unsigned long long int myIv = 36753562;                             // Vecteur d'initialisation

void aesSetup() {
  printf_begin();
  radio.begin(); 
  radio.openWritingPipe(addresses[0]); // 00002 
  radio.openReadingPipe(1, addresses[1]); // 00001 
  radio.setPALevel(RF24_PA_MIN); 
}
