
#include <LowPower.h>
#define ledPin 13    // output pin for the LED (to show it is awake)
int sensorSoil1 = A0;
void setup() {
  Serial.begin(9600);
  pinMode(ledPin,OUTPUT);
  digitalWrite(ledPin,LOW);
}

void loop() {
  Serial.println("Blink");
  delay(1000);
  int soil1 = getSoil1();
  Serial.println(soil1);
  doBlink();

  delay(2000);
  Serial.println("Arduino:- I am going for a Nap");
  delay(200);
  digitalWrite(LED_BUILTIN,LOW);
  LowPower.idle(SLEEP_8S, ADC_OFF, TIMER2_OFF, TIMER1_OFF, TIMER0_OFF, SPI_OFF, USART0_OFF, TWI_OFF);
  LowPower.powerDown(SLEEP_8S, ADC_OFF, BOD_OFF);
  Serial.println("Arduino:- Hey I just Woke up");
  Serial.println("");
  delay(2000);
}

int getSoil1()
{
  delay(200);
  int valueSoil1 = analogRead(sensorSoil1);
  return valueSoil1;
}

void doBlink() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, LOW);
  delay(2000);
  digitalWrite(ledPin, HIGH);
  delay(10);
  digitalWrite(ledPin, LOW);
}


//Dry 595
//Water 259 
