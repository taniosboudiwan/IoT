#include <SPI.h>
#include <RH_RF95.h>

// Singleton instance of the radio driver
RH_RF95 rf95;

// Define frequency
float frequency = 868.1;

// Initialize the frame number counter
unsigned int trameNumber = 0;

void setup()
{
  Serial.begin(115200);
  while (!Serial) ; // Wait for serial port to be available
  //Serial.println("initialization");
  
  if (!rf95.init())
    Serial.println("init failed");

  rf95.setFrequency(frequency);
  rf95.setTxPower(13);
  rf95.setSpreadingFactor(7);
  rf95.setSignalBandwidth(125000);
  rf95.setCodingRate4(5);
}

void loop()
{
  //Serial.println("Sending to rf95_server");

  // Create the JSON message with dev_id and trameNumber
  String message = "{\"dev_id\":\"L-27\", \"trameNumber\":" + String(trameNumber) + "}";
  
  // Convert the message to a byte array
  uint8_t data[message.length() + 1];
  message.getBytes(data, sizeof(data));
  
  // Send the JSON message
  rf95.send(data, sizeof(data));
  rf95.waitPacketSent();
  
  Serial.println(message);

  // Increment trameNumber for the next message
  trameNumber++;
  
  // Wait 10 seconds before sending the next message
  delay(10000);
}