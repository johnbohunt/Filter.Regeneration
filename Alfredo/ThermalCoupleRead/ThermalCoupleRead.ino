int Count = 0;        // Counter variable to keep track of the number of readings
float Voltage = 0;    // Variable to store the accumulated voltage readings

void setup() {
  Serial.begin(9600); // Initialize serial communication at a baud rate of 9600
}

// Function to convert ADC value to voltage
float ConvertADCtoVoltage(float ADCValue) {
  float ConvertingConst = 5.0 / 1023.0; // Conversion constant based on ADC resolution
  return (ConvertingConst * ADCValue);  // Calculate and return the voltage value
}

// Function to read the resistance temperature detector (RTD)
int ReadRTD(const int RTD) {
  float value;
  value = analogRead(RTD); // Read the analog value from the specified RTD pin
  return value;            // Return the analog value
}

// Function to calculate temperature from voltage using the original equation
float GetTemp(float volt) {
  float slope = 99.9;   // Slope of the temperature-voltage relationship (V/C)
  float b = 32.4;      // Intercept of the temperature-voltage relationship
  float temp = (volt * slope) + b;  // Calculate the temperature in Celsius
  return temp;   // Return the temperature value
}

// Function to calculate "NewTemp" based on the ADC value using a new equation
float CalculateNewTemp(float ADCValue) {
  float slope = 1.9797;   // Slope of the new equation
  float b = 39.104;       // Intercept of the new equation
  float temp = (slope * ADCValue) + b;  // Calculate the "NewTemp"
  return temp;   // Return the "NewTemp" value
}

void loop() {
  if (Count < 30) {   // Take 30 readings
    Voltage = (Voltage + ConvertADCtoVoltage(ReadRTD(A2))); // Accumulate the voltage readings
    Count = Count + 1;  // Increment the count
  } else {
    float AverageVoltage;
    AverageVoltage = Voltage / Count;  // Calculate the average voltage
    
    // Print the average voltage, raw ADC reading, temperature, and "NewTemp"
    Serial.print(AverageVoltage);
    Serial.print(" ");
    Serial.print(ReadRTD(A2));
    Serial.print(" ");
    Serial.print(GetTemp(AverageVoltage));
    Serial.print(" ::: ");
    Serial.println(CalculateNewTemp(ReadRTD(A2)));
    
    Count = 0;    // Reset the count
    Voltage = 0;  // Reset the accumulated voltage
  }
  delay(10);   // Delay for 10 milliseconds
}
