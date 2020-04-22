void radioCom() {
  switch(mode) {
    // Mode controle manuel
    case 1:
      Serial.println("Mode controle manuel");
      radio.startListening(); 
      while (radio.available()){ 
        radio.read(&rc, sizeof(rc));
      }
      radio.stopListening();
      mspCom();
      radio.write(&values, sizeof(values));
    break;

    // Mode return to home
    case 2:
      Serial.println("Mode return to home");
      
    break;

    // Mode ouverture du garage
    case 3:
      Serial.println("Mode ouverture du garage");
      
    break;
  }
}
