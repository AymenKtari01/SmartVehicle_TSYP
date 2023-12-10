// Includes the Servo library
#include <Servo.h>
#include <Wire.h>
#include <VL53L0X.h>
VL53L0X sensor;

// Variables for the duration and the distance
int distance;
Servo myServo; // Creates a servo object for controlling the servo motor
void setup() {
  Wire.begin();
  
  // Initialize the sensor
  if (!sensor.init()) {
    Serial.println("Failed to initialize VL53L0X sensor!");
    while (1);
  } 
  // Start continuous measurement
  sensor.startContinuous();
  Serial.begin(9600);
  myServo.attach(2); // Defines on which pin is the servo motor attached
}
void loop() {
  // rotates the servo motor from 15 to 165 degrees
  for(int i=15;i<=165;i+=5){  
  myServo.write(i);
  delay(10);
  distance = sensor.readRangeContinuousMillimeters()/10;
  
  Serial.print(i); // Sends the current degree into the Serial Port
  Serial.print(","); // Sends addition character right next to the previous value needed later in the Processing IDE for indexing
  Serial.print(distance); // Sends the distance value into the Serial Port
  Serial.print("."); // Sends addition character right next to the previous value needed later in the Processing IDE for indexing
  }
  // Repeats the previous lines from 165 to 15 degrees
  for(int i=165;i>15;i-=5){  
  myServo.write(i);
  delay(10);
  distance = sensor.readRangeContinuousMillimeters()/10;
  Serial.print(i);
  Serial.print(",");
  Serial.print(distance);
  Serial.print(".");
  }
}
