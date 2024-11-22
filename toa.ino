#include <SPI.h>
#include <RH_RF95.h>

// Singleton instance of the radio driver
RH_RF95 rf95;

// Frequency for the LoRa communication
float frequency = 868.1;

// Variable pour compter les messages envoyés
int messageCount = 0;
unsigned long lastSendTime = 0; // Enregistre l'heure d'envoi du dernier message

void setup()
{
  Serial.begin(115200);
  while (!Serial); // Wait for serial port to be available
  Serial.println("initialization");
  if (!rf95.init())
    Serial.println("init failed");

  rf95.setFrequency(frequency);
  rf95.setTxPower(13);
  rf95.setSpreadingFactor(8);
  rf95.setSignalBandwidth(62500);
  rf95.setCodingRate4(5);
}

void loop()
{
  // Vérifier si 5 secondes se sont écoulées depuis le dernier envoi
  if (millis() - lastSendTime >= 5000)
  {
    Serial.println("Sending to rf95_server");

    // Préparer le message
    uint8_t data[] = "Hello World";
    Serial.println(sizeof(data));

    // Mesurer le temps de vol
    unsigned long toa = measureToA(data, sizeof(data));
    Serial.print("Time on Air: ");
    Serial.print(toa);
    Serial.println(" microseconds");

    // Suivre l'envoi du message
    messageCount++;  // Incrémente le compteur de messages
    Serial.print("Message #");
    Serial.print(messageCount);
    Serial.println(" sent successfully.");

    // Enregistrer l'horodatage actuel
    lastSendTime = millis(); // Mettre à jour le dernier temps d'envoi
    Serial.print("Timestamp (ms): ");
    Serial.println(lastSendTime);
  }

  // Faire d'autres tâches si nécessaire pendant que l'intervalle de 5 secondes est en attente
}

// Fonction pour mesurer le temps de vol (ToA) en microsecondes
unsigned long measureToA(uint8_t* data, uint8_t dataSize)
{
  unsigned long start = micros(); // Enregistrer le temps de début
  rf95.send(data, dataSize);      // Envoyer le paquet
  rf95.waitPacketSent();          // Attendre que le paquet soit entièrement transmis
  unsigned long end = micros();   // Enregistrer le temps de fin
  return end - start;             // Calculer et retourner le ToA
}