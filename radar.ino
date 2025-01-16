#include <Servo.h>  

// Pin definitions
const int trigPin = 9;    // Ultrasonic sensor trigger pin
const int echoPin = 8;    // Ultrasonic sensor echo pin
const int servoPin = 10;  // Servo motor control pin
const int speakerPin = 3; // Speaker pin for beep sound

Servo myServo; // Servo motor object

// Variables to hold measurement data
float duration_us, distance_cm;
int angle = 0; // Servo motor angle

void setup() {
  // Initialize servo motor
  myServo.attach(servoPin);
  
  // Configure pin modes
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(speakerPin, OUTPUT);

  // Initialize serial communication for debugging
  Serial.begin(9600);
  Serial.println("Radar System Initialized");
}

/* 
  Main loop:
  - Rotates the servo motor from 0° to 180° and back.
  - Measures distance at each step and logs the results.
*/
void loop() {
  // Sweep servo from 0° to 180°
  for (angle = 0; angle <= 180; angle += 2) {
    myServo.write(angle);   // Move servo to the current angle
    delay(30);              // Wait for the servo to reach the position
    measureDistance();      // Measure and log the distance
  }

  // Sweep servo back from 180° to 0°
  for (angle = 180; angle >= 0; angle -= 2) {
    myServo.write(angle);   // Move servo to the current angle
    delay(30);              // Wait for the servo to reach the position
    measureDistance();      // Measure and log the distance
  }
}

/*
  Function: beepSpeaker
  - Emits a short beep sound using the speaker.
*/
void beepSpeaker() {
  tone(speakerPin, 1000, 30); // Play tone at 1000 Hz for 30 ms
  delay(10);                  // Short delay to avoid overlapping sounds
}

/*
  Function: measureDistance
  - Sends an ultrasonic pulse and calculates the distance to an object.
  - Logs the measured distance and angle to the serial monitor.
*/
void measureDistance() {
  // Send an ultrasonic pulse
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Measure the duration of the echo
  duration_us = pulseIn(echoPin, HIGH);

  // Calculate the distance in centimeters
  distance_cm = duration_us * 0.0343 / 2;

  // Log the angle and distance
  Serial.print("Angle: ");
  Serial.print(angle);
  Serial.print(", Distance: ");

  // Handle out-of-range readings
  if (duration_us == 0) {
    Serial.println("Out of Range");
  } else {
    Serial.println(distance_cm);
  }
}
