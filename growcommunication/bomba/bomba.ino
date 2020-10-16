const int pin = 9;
 
void setup()
{
  pinMode(pin, OUTPUT);
}
 
void loop()
{
  if ( bt.available() > 0 ) {
    int count = bt.parseInt();
    if (count > 0) {
      Pump(count);
    }
  }

}

void Pump(int count){
  digitalWrite(pin, HIGH);   // poner el Pin en HIGH
  delay(10000);               // esperar 10 segundos
  digitalWrite(pin, LOW);    // poner el Pin en LOW
  delay(10000);               // esperar 10 segundos
  }
