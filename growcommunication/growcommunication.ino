

//This sketch will use bluetooth to send temperature and humidity
// to a Raspberry PI using bluetooth
// Arduino -> bluetooth
#include <SoftwareSerial.h> //Serial library
#include <Sleep_n0m1.h>
#include <DHT.h>
#include <OneWire.h>                
#include <DallasTemperature.h>
#define DHTPIN 2       //Where is DHT connected
#define DHTTYPE DHT22 // Type of sensor used
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
OneWire ourWire1(3); 
OneWire ourWire2(4); 
OneWire ourWire3(5); 
OneWire ourWire4(6); 
OneWire ourWire5(7);              
DallasTemperature sensors1(&ourWire1);
DallasTemperature sensors2(&ourWire2);
DallasTemperature sensors3(&ourWire3);
DallasTemperature sensors4(&ourWire4);
DallasTemperature sensors5(&ourWire5);


SoftwareSerial bt(0, 1); //RX, TX (Switched on the Bluetooth – RX -> TX | TX -> RX)
int btdata;              // the data given from the computer
DHT dht(DHTPIN, DHTTYPE);
void setup()
{
  sensors1.begin(); 
  sensors2.begin(); 
  sensors3.begin(); 
  sensors4.begin(); 
  sensors5.begin();   
  bt.begin(9600);
  dht.begin(); 
  //sleepTime = 500;
  sleepTime = 1800000;
  
}

void loop()
{
  count++;
  delay(2000);  
  int soil = getSoil();
  int luz = getLight();
  float hh = getHumid();
  float tt = getTemp();
  delay(2000);  
  sensors1.requestTemperatures();   //Se envía el comando para leer la temperatura
  float temp1= sensors1.getTempCByIndex(0);
  delay(2000);  
  sensors2.requestTemperatures();   //Se envía el comando para leer la temperatura
  float temp2= sensors2.getTempCByIndex(0);
  delay(2000); 
  sensors3.requestTemperatures();   //Se envía el comando para leer la temperatura
  float temp3= sensors3.getTempCByIndex(0);
  delay(2000); 
  sensors4.requestTemperatures();   //Se envía el comando para leer la temperatura
  float temp4= sensors4.getTempCByIndex(0);
  delay(2000);
  sensors5.requestTemperatures();   //Se envía el comando para leer la temperatura
  float temp5= sensors5.getTempCByIndex(0);
  delay(2000);  
  //float ts = getSoilTemperature(sensors);
  //Serial.println(hh);
  //Serial.println(tt);
  if (count >= 4)
  {
    bt.print("H:" + String(hh) + ",T:" + String(tt) + ",L:" + String(luz) + ",HS:" + String(soil) + ",TS1:" + String(temp1)+ ",TS2:" + String(temp2)+ ",TS3:" + String(temp3)+ ",TS4:" + String(temp4)+ ",TS5:" + String(temp5));
    bt.print("\n");
  }

  if (count >= 5)
  {
    count = 0;
    Serial.print("sleeping ");
    Serial.println(sleepTime);
    delay(100); //delay to allow serial to fully print before sleep
    //sleep.standbyMode();
    sleep.pwrDownMode(); //set sleep mode
    sleep.sleepDelay(sleepTime); //sleep for: sleepTime
  }
}

//FUNCTIONS
float getHumid()
{
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds ‘old’ (its a very slow sensor)
  delay(200);
  return (float)dht.readHumidity();
}
float getTemp()
{
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds ‘old’ (its a very slow sensor)
  delay(200);
  return (float)dht.readTemperature();
}
int getLight()
{
  delay(200);
  valueLDR = analogRead(sensorLDR);
  return valueLDR;
}
int getSoil()
{
  delay(200);
  valueSoil = analogRead(sensorSoil);
  return valueSoil;
}

//float getSoilTemperature(sensors)
//{
//  delay(200);
//  sensors.requestTemperatures();   //Se envía el comando para leer la temperatura
//  float temp= sensors.getTempCByIndex(0); //Se obtiene la temperatura en ºC
//  return temp;
//}
