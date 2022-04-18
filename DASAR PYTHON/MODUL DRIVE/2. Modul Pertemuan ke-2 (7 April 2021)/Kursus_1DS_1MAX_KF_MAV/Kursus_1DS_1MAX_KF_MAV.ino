//betulin coding MAV bermasalah dan cek di parallax
#include <max6675.h>
#include <cactus_io_DS18B20.h>
#include <SimpleKalmanFilter.h>
#include <movingAvg.h> 

int pinDS[1] = {A1};                                       //DS18S20 Signal pin on analog 1
MAX6675 thermocouple[1] = {MAX6675(4,3,2)};                //sck cs so

int Counter = 0;
movingAvg avgTemp(3);                                     // define the moving average object

float tds[1] = {0};
float tcmentah[1] = {0};
float tckalman[1] = {0};
float tcmav[1] = {0};
//float tckalmankalibrasi[1] = {0};
SimpleKalmanFilter KF1(0.9, 10, 0.3);

void setup()
{
  Serial.begin(9600);
  avgTemp.begin();
}

void loop()
{
  delay(500);
  Serial.print("DATA, DATE, TIME,");
  Counter = Counter + 1;
  Serial.print(Counter);
 
    for (int i = 0; i < 1; i++)
  {
    DS18B20 ds(pinDS[i]);
    ds.readSensor();
    tds[i] = ds.getTemperature_C();
    Serial.print(", T ds");
    Serial.print(tds[i], 4);
  }

  for (int i = 0; i < 1; i++)
  {
    tcmentah[i] = thermocouple[i].readCelsius();
    tcmav[i] = avgTemp.reading(tcmentah[i]);
    Serial.print(", T tc Mentah ");
    Serial.print(tcmentah[i], 4);
    Serial.print(", T tc mav");
    Serial.print(tcmav[i]);
  }

  
  for (int i = 0; i < 1; i++)
 {
    switch (i)
    {
      case 0:
      tckalman[i] = KF1.updateEstimate(tcmentah[i]);
    //tckalmankalibrasi[i] = (0.9575 * tckalman[i]) - 0.6395;
      break;
    /* case 1:
      tckalman[i] = KF2.updateEstimate(tcmentah[i]);
    //tckalmankalibrasi[i] = (0.9575 * tckalman[i]) - 0.6395;
      break;*/
      default:
      break;
    }
    
    Serial.print(", T tc kalman ");
    Serial.print(tckalman[i], 2);
  //Serial.print(", T ttc kalman ");
  //Serial.print(tckalmankalibrasi[i], 2);
 }
  
  if (Counter >= 9999999)
  {
    Counter = 0;
  }
  Serial.println();
  delay(300);
}
