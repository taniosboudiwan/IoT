void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  sendSOS(); // Appelle la fonction pour envoyer "SOS" en Morse
  delay(3000); // Attendre 3 secondes avant de répéter
}

void sendSOS() {
  for (int i = 0; i < 3; i++) { // Envoie les 3 courts pour "S"
    blinkDot();
  }
  for (int i = 0; i < 3; i++) { // Envoie les 3 longs pour "O"
    blinkDash();
  }
  for (int i = 0; i < 3; i++) { // Envoie les 3 courts pour "S"
    blinkDot();
  }
}

void blinkDot() { // Court clignotement
  digitalWrite(LED_BUILTIN, HIGH);
  delay(200);
  digitalWrite(LED_BUILTIN, LOW);
  delay(200);
}

void blinkDash() { // Long clignotement
  digitalWrite(LED_BUILTIN, HIGH);
  delay(600);
  digitalWrite(LED_BUILTIN, LOW);
  delay(200);
}
