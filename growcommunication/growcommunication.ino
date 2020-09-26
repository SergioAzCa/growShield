



//This sketch will use bluetooth to send temperature and humidity
// to a Raspberry PI using bluetooth
// Arduino -> bluetooth
#include <SoftwareSerial.h> //Serial library
#include <Sleep_n0m1.h>
#include <DHT.h>
#define DHTPIN 2  //Where is DHT connected
#define DHTTYPE DHT22  // Type of sensor used
/**
* Arduino connection HC-05 connection:
* HC-05  | Arduino
* TX     | 0
* RX     | 1
*/
int count = 0;
Sleep sleep;
unsigned long sleepTime; //how long you want the arduino to sleep
int sensorLDR = A0;
int sensorSoil = A1;
int valueLDR = 0;
int valueSoil = 0;

SoftwareSerial bt (0,1);  //RX, TX (Switched on the Bluetooth – RX -> TX | TX -> RX)
int btdata; // the data given from the computer
DHT dht(DHTPIN, DHTTYPE);
void setup() {
  bt.begin(9600);
  sleepTime = 50000; 
  dht.begin();
  
}


void loop() {
    count++;
    delay(200);
    int soil= getSoil();
    int luz = getLight();
    float hh = getHumid();
    float tt = getTemp();
    //Serial.println(hh);
    //Serial.println(tt);
    if(count >=4)
        bt.print ("H:"+String(hh) + ",T:" + String(tt)+",L:"+String(luz)+",HS:"+String(soil)+",TS:null,end");
        bt.print("\n");
    if(count >= 5)
    {
        count = 0;
        Serial.print("sleeping ");
        Serial.println(sleepTime); 
        delay(100); //delay to allow serial to fully print before sleep
        sleep.standbyMode();
        //sleep.pwrDownMode(); //set sleep mode
        sleep.sleepDelay(sleepTime); //sleep for: sleepTime
    }

   
}




//FUNCTIONS
float getHumid() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds ‘old’ (its a very slow sensor)
  delay(200);
  return (float)dht.readHumidity();
}
float getTemp() {
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds ‘old’ (its a very slow sensor)
  delay(200);
  return (float)dht.readTemperature();
}
int getLight(){
  delay(200);
  valueLDR = analogRead(sensorLDR);
  return valueLDR;
}
int getSoil(){
  delay(200);
  valueSoil =  analogRead(sensorSoil);
  return valueSoil;

}
