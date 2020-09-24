//This sketch will use bluetooth to send temperature and humidity
// to a Raspberry PI using bluetooth
// Arduino -> bluetooth
#include <SoftwareSerial.h> //Serial library
#include <DHT.h>
#define DHTPIN 2  //Where is DHT connected
#define DHTTYPE DHT22  // Type of sensor used
/**
* Arduino connection HC-05 connection:
* HC-05  | Arduino
* TX     | 0
* RX     | 1
*/

int sensorLDR = A0;
int sensorSoil = A1;
int valueLDR = 0;
int valueSoil = 0;

SoftwareSerial bt (0,1);  //RX, TX (Switched on the Bluetooth – RX -> TX | TX -> RX)
int btdata; // the data given from the computer
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  bt.begin(9600);
  /* Since we run out of 5v PIN
  * and don’t wanna use a breadboard – the VCC of the DHT22
  * is connected to PIN 8
  * And we just use digitalWrite to put it HIGH
  */
  //pinMode(8, OUTPUT); //explained above why PIN 8
  //digitalWrite(8,HIGH);
  dht.begin();
}

void loop() {
    int soil= getSoil();
    int luz = getLight();
    float hh = getHumid();
    float tt = getTemp();
    //Serial.println(hh);
    //Serial.println(tt);
    bt.print ("H:"+String(hh) + ",T:" + String(tt)+",L:"+String(luz)+",HS:"+String(soil)+",TS:null");
    bt.print("\n");
    delay (900000); //prepare for data (2s)
}
float getHumid() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds ‘old’ (its a very slow sensor)
  return (float)dht.readHumidity();
}
float getTemp() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds ‘old’ (its a very slow sensor)
  return (float)dht.readTemperature();
}
int getLight(){
  valueLDR = analogRead(sensorLDR);
  return valueLDR;
}
int getSoil(){
  valueSoil =  analogRead(sensorSoil);
  return valueSoil;

}
