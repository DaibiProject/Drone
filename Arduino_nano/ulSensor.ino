void ulSensor() {
  /* Lance une mesure de distance en envoyant une impulsion HIGH de 10µs sur la broche TRIGGER */
  // Devant
    digitalWrite(TRIGGER_ULSF, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_ULSF, LOW);
  // Gauche
    digitalWrite(TRIGGER_ULSL, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_ULSL, LOW);
  // Derriere
    digitalWrite(TRIGGER_ULSB, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_ULSB, LOW);
  // Droite
    digitalWrite(TRIGGER_ULSR, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_ULSR, LOW);
  // Ground
    digitalWrite(TRIGGER_ULSG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIGGER_ULSG, LOW);
    
  /* Mesure le temps entre l'envoi de l'impulsion ultrasonique et son écho (si il existe) */
  long measure_front      =   pulseIn(ECHO_ULSF, HIGH, MEASURE_TIMEOUT);
  long measure_left       =   pulseIn(ECHO_ULSL, HIGH, MEASURE_TIMEOUT);
  long measure_back       =   pulseIn(ECHO_ULSB, HIGH, MEASURE_TIMEOUT);
  long measure_right      =   pulseIn(ECHO_ULSR, HIGH, MEASURE_TIMEOUT);
  long measure_ground     =   pulseIn(ECHO_ULSG, HIGH, MEASURE_TIMEOUT);
  
  /* Calcul la distance à partir du temps mesuré */
  float d_front           =   measure_front / 2.0 * SOUND_SPEED;
  float d_left            =   measure_left / 2.0 * SOUND_SPEED;
  float d_back            =   measure_back / 2.0 * SOUND_SPEED;
  float d_right           =   measure_right / 2.0 * SOUND_SPEED;
  float d_ground          =   measure_ground / 2.0 * SOUND_SPEED;
  
  /* Affiche les résultats en mm, cm et m */
  //  Serial.print(F("Distance: "));
  //  Serial.print(distance_mm);
  //  Serial.print(F("mm ("));
  //  Serial.print(distance_mm / 10.0, 2);
  //  Serial.print(F("cm, "));
  //  Serial.print(distance_mm / 1000.0, 2);
  //  Serial.println(F("m)"));
   
  /* Délai d'attente pour éviter d'afficher trop de résultats à la seconde */
  //  delay(500);

  if (d_front < 10) {
    LVL_FRONT = 3;
  } else if (d_front < 15) {
    LVL_FRONT = 2;
  } else if (d_front < 20) {
    LVL_FRONT = 1;
  } else {
    LVL_FRONT = 0;
  }
  if (d_left < 10) {
    LVL_LEFT = 3;
  } else if (d_left < 15) {
    LVL_LEFT = 2;
  } else if (d_left < 20) {
    LVL_LEFT = 1;
  } else {
    LVL_LEFT = 0;
  }
  if (d_back < 10) {
    LVL_BACK = 3;
  } else if (d_back < 15) {
    LVL_BACK = 2;
  } else if (d_back < 20) {
    LVL_BACK = 1;
  } else {
    LVL_BACK = 0;
  }
  if (d_right < 10) {
    LVL_RIGHT = 3;
  } else if (d_right < 15) {
    LVL_RIGHT = 2;
  } else if (d_right < 20) {
    LVL_RIGHT = 1;
  } else {
    LVL_RIGHT = 0;
  }
  if (d_ground < 10) {
    LVL_GROUND = 3;
  } else if (d_ground < 15) {
    LVL_GROUND = 2;
  } else if (d_ground < 20) {
    LVL_GROUND = 1;
  } else {
    LVL_GROUND = 0;
  }
  
}
