#include <cactus_io_DS18B20.h>

int pinDS[1] = {A1};                                       //DS18S20 Signal pin on analog 1 & 2
int Counter = 0;

float tds[1] = {0};

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  delay(1000);
  Serial.print("DATA, DATE, TIME,");
  Counter = Counter + 1;
  Serial.print(Counter);
 
    for (int i = 0; i < 1; i++)
  {
    DS18B20 ds(pinDS[i]);
    ds.readSensor();
    tds[i] = ds.getTemperature_C();
    //DSavg = DSavg + tds[i];
    Serial.print(", ");
    Serial.print("DS: ");
    Serial.print (tds[i], 4);
  }

    if (Counter >= 9999999)
  {
    Counter = 0;
  }
  Serial.println();
  delay(300);
}
