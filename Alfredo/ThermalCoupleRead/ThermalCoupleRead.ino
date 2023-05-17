int Count=0;
float Voltage=0;
void setup() {
  // put your setup code here, to run once:
 // put your setup code here, to run once:
  Serial.begin(9600);
}
float ConvertADCtoVoltage(float ADCValue)
{
  float ConvertingConst = 5.0/1023.0;
  return   (ConvertingConst*ADCValue);
}
int ReadRTD(const int RTD){
    float value;
    value = analogRead(RTD);
    return value;
  }
  float GetTemp(float volt){
    float temp,slope,b;
    slope=99.9; // V/C
    b=32.4;
    //if(volt<=0.08)
      //temp=(slope*volt)-b; // In C
    //else
    temp=(volt*slope)+b; // In C
    return (temp) ;
  }
void loop() {
  // put your main code here, to run repeatedl:
      if(Count<30){
        Voltage=(Voltage+ConvertADCtoVoltage(ReadRTD(A2)));
        Count=Count+1;
      }else{
          float AverageVoltage;
          AverageVoltage=Voltage/Count;
          
          Serial.print(AverageVoltage);
          Serial.print(" ");
          Serial.print(ReadRTD(A2));
          Serial.print(" ");
          Serial.println(GetTemp(AverageVoltage));

        
          Count=0;
          Voltage=0;
        }
        delay(10);
}
