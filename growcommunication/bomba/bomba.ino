const int pin = 9;
 
void setup()
{
  pinMode(pin, OUTPUT);  //definir pin como salida
}
 
void loop()
{
  digitalWrite(pin, HIGH);   // poner el Pin en HIGH
  delay(10000);               // esperar 10 segundos
  digitalWrite(pin, LOW);    // poner el Pin en LOW
  delay(10000);               // esperar 10 segundos
}