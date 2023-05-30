const int analogPin = A2;  // ADC input pin
const int numSamples = 50; // Number of samples to take

// Conversion equation constants
const float slope = 1.2617;
const float intercept = 41.132;

// Desired temperature
const float desiredTemperature = 50.0; // Desired temperature in Celsius

float averageTemperature = 0.0; // Average temperature based on previous measurements
float timeConstant = 0.0;       // Time constant for approaching the desired temperature

void setup() {
  Serial.begin(9600);  // Initialize serial communication
  analogReference(DEFAULT); // Set the default reference voltage (5V)
}

void loop() {
  int total = 0;

  // Take 50 samples and sum them up
  for (int i = 0; i < numSamples; i++) {
    total += analogRead(analogPin);
    delay(10); // Delay between each sample (adjust if needed)
  }

  // Calculate the average ADC value
  float average = (float)total / numSamples;

  // Convert ADC value to temperature
  float temperature = slope * average + intercept;

  // Update average temperature using previous measurements
  averageTemperature = (averageTemperature * 9.0 + temperature) / 10.0;

  // Calculate the time constant if it hasn't been calculated yet
  if (timeConstant == 0.0 && averageTemperature != desiredTemperature) {
    timeConstant = 1.0 / abs(averageTemperature - desiredTemperature);
  }

  // Print the average ADC value
  Serial.print("Average ADC value: ");
  Serial.println(average);

  // Print the temperature in Celsius
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");

  // Print the calculated time constant
  if (timeConstant != 0.0) {
    Serial.print("Time Constant: ");
    Serial.print(timeConstant);
    Serial.println(" sec");
  }

  delay(1000);  // Delay before taking the next set of samples
}
