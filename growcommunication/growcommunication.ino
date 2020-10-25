#include <SoftwareSerial.h> //Serial library
//#include <LowPower.h>
#include <Sleep_n0m1.h>
#include <DHT.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#define DHTPIN 2      //Where is DHT connected
#define DHTTYPE DHT22 // Type of sensor used
/**
  Arduino connection HC-05 connection:
  HC-05  | Arduino
  TX     | 0
  RX     | 1
*/
int count = 0;
int ledInterno = 13;
const int pin = 9; //Bomba
Sleep sleep;
//unsigned long sleepTime; //how long you want the arduino to sleep
int sensorLDR = A0;
int sensorSoil1 = A1;
int sensorSoil2 = A2;
int sensorSoil3 = A3;
int sensorSoil4 = A4;
int sensorSoil5 = A5;
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
unsigned long sleepTime;
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
  digitalWrite(ledInterno, LOW);
  delay(1000);
  if (count == 4)
  {
    int soil1 = getSoil1();
    int soil2 = getSoil2();
    int soil3 = getSoil3();
    int soil4 = getSoil4();
    int soil5 = getSoil5();
    delay(2000);
    int luz = getLight();
    float hh = getHumid();
    float tt = getTemp();
    delay(1000);
    sensors1.requestTemperatures(); //Se envía el comando para leer la temperatura
    float temp1 = sensors1.getTempCByIndex(0);
    delay(1000);
    sensors2.requestTemperatures(); //Se envía el comando para leer la temperatura
    float temp2 = sensors2.getTempCByIndex(0);
    delay(1000);
    sensors3.requestTemperatures(); //Se envía el comando para leer la temperatura
    float temp3 = sensors3.getTempCByIndex(0);
    delay(1000);
    sensors4.requestTemperatures(); //Se envía el comando para leer la temperatura
    float temp4 = sensors4.getTempCByIndex(0);
    delay(1000);
    sensors5.requestTemperatures(); //Se envía el comando para leer la temperatura
    float temp5 = sensors5.getTempCByIndex(0);
    delay(1000);
    bt.print("H:" + String(hh) + ",T:" + String(tt) + ",L:" + String(luz) + ",HS1:" + String(soil1) + ",HS2:" + String(soil2) + ",HS3:" + String(soil3) + ",HS4:" + String(soil4) + ",HS5:" + String(soil5) + ",TS1:" + String(temp1) + ",TS2:" + String(temp2) + ",TS3:" + String(temp3) + ",TS4:" + String(temp4) + ",TS5:" + String(temp5));
    bt.print("\n");
  }
  if (count == 5)
  {
    count = 0;
    //delay(100); //delay to allow serial to fully print before sleep
    //sleep.standbyMode();
    sleep.pwrDownMode();         //set sleep mode
    sleep.sleepDelay(sleepTime); //sleep for: sleepTime
    //    for (int sleepCounter = 113; sleepCounter > 0; sleepCounter--)
    //    {
    //      LowPower.idle(SLEEP_8S,ADC_ON, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_OFF, TWI_OFF);
    //      LowPower.powerDown(SLEEP_8S,ADC_ON, BOD_OFF);
    //    }
  }
  count++;
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
int getSoil1()
{
  delay(2000);
  int valueSoil1 = analogRead(sensorSoil1);
  pumpWater(valueSoil1);
  return valueSoil1;
}
int getSoil2()
{
  delay(2000);
  int valueSoil2 = analogRead(sensorSoil2);
  pumpWater(valueSoil2);
  return valueSoil2;
}
int getSoil3()
{
  delay(2000);
  int valueSoil3 = analogRead(sensorSoil3);
  pumpWater(valueSoil3);
  return valueSoil3;
}
int getSoil4()
{
  delay(2000);
  int valueSoil4 = analogRead(sensorSoil4);
  pumpWater(valueSoil4);
  return valueSoil4;
}
int getSoil5()
{
  delay(2000);
  int valueSoil5 = analogRead(sensorSoil5);
  pumpWater(valueSoil5);
  return valueSoil5;
}

int pumpWater(int soil)
{
  const int AirValue = 594;
  const int WaterValue = 259;
  int intervals = (AirValue - WaterValue) / 3;
  int soilMoistureValue = 0;
  if (soil < AirValue && soil > (AirValue - intervals))
  {
    Pump();
  }
  delay(1000);
}
void Pump()
{
  digitalWrite(pin, HIGH); // poner el Pin en HIGH
  delay(10000);            // esperar 10 segundos
  digitalWrite(pin, LOW);  // poner el Pin en LOW
  delay(10000);            // esperar 10 segundos
}
//float getSoilTemperature(sensors)
//{
//  delay(200);
//  sensors.requestTemperatures();   //Se envía el comando para leer la temperatura
//  float temp= sensors.getTempCByIndex(0); //Se obtiene la temperatura en ºC
//  return temp;
//}
