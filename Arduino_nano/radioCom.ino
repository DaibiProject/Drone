bool radioCom(int mode) {
  switch(mode) {
    // Mode controle manuel
    case 1:
      Serial.println("Mode controle manuel");
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
