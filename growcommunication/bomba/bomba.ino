#include <SoftwareSerial.h> //Serial library
const int pin = 9;
 SoftwareSerial bt(0, 1);
void setup()
{
  bt.begin(9600);
  pinMode(pin, OUTPUT);
}
 
void loop(){
  
      Pump(
        );
   
 

}

void Pump(){
  digitalWrite(pin, HIGH);   // poner el Pin en HIGH
  delay(20000);               // esperar 10 segundos
  digitalWrite(pin, LOW);    // poner el Pin en LOW
  delay(10000);               // esperar 10 segundos
  }
