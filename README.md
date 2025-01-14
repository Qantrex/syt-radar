# Arduino Radar System with Ultrasonic Sensor and Servo Motor

## Overview

This Arduino sketch implements a radar-like system that uses an ultrasonic sensor, a servo motor, and a speaker. The servo motor sweeps the ultrasonic sensor back and forth, measuring distances and displaying them on the serial monitor. A speaker produces a short beep for each distance measurement.

## Components Used

1. **Ultrasonic Sensor**  
   - Measures the distance to an object by emitting ultrasonic waves and calculating the time it takes for the echo to return.
   
2. **Servo Motor**  
   - Rotates the ultrasonic sensor to scan a range of angles (0° to 180° and back).
   
3. **Speaker**  
   - Emits a sound indicating that a distance measurement has been taken.

4. **Arduino Board**  
   - Microcontroller to control the components and process the logic.

## Pin Connections

| Component         | Arduino Pin |
|--------------------|-------------|
| Ultrasonic Trig    | 9           |
| Ultrasonic Echo    | 8           |
| Servo Signal       | 10          |
| Speaker Positive   | 3           |

## Code Breakdown

### Libraries Used
```cpp
#include <Servo.h>
```
- The `Servo` library is included to control the servo motor.

---

### Global Variables and Constants

1. **Pins**:
   - `trigPin`, `echoPin`, `servoPin`, `speakerPin`: Define the respective pins for components.
   
2. **Servo Object**:
   - `myServo`: Creates a servo object to control the servo motor.
   
3. **Distance Variables**:
   - `duration_us`: Time in microseconds for the ultrasonic pulse to return.
   - `distance_cm`: Calculated distance in centimeters.

4. **Angle**:
   - `angle`: Stores the current angle of the servo motor.

---

### Setup Function
```cpp
void setup() {
    myServo.attach(servoPin);  
    pinMode(trigPin, OUTPUT);  
    pinMode(echoPin, INPUT);   
    pinMode(speakerPin, OUTPUT); 
    Serial.begin(9600);        
    Serial.println("Radar System Initialized");
}
```
- **Servo Initialization**: Attaches the servo motor to the `servoPin`.
- **Pin Modes**: Configures ultrasonic sensor pins and speaker as `OUTPUT` or `INPUT`.
- **Serial Communication**: Initializes communication at a baud rate of 9600 and prints a startup message.

---

### Main Loop
```cpp
void loop() {
    for (angle = 0; angle <= 180; angle += 2) {
        myServo.write(angle);   
        delay(30);              
        measureDistance();      
    }

    for (angle = 180; angle >= 0; angle -= 2) {
        myServo.write(angle);
        delay(30);
        measureDistance();
    }
}
```
- The loop performs a sweeping motion with the servo motor:
  - Moves from 0° to 180° and back to 0° in 2° increments.
  - Calls `measureDistance()` at each angle to measure and log the distance.

---

### Distance Measurement
```cpp
void measureDistance() {
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);

    duration_us = pulseIn(echoPin, HIGH);
    distance_cm = duration_us * 0.0343 / 2;  

    Serial.print("Angle: ");
    Serial.print(angle);
    Serial.print(", Distance: ");
    if (duration_us == 0) {
        Serial.println("Out of Range");
    } else {
        Serial.println(distance_cm);
    }
}
```
- **Ultrasonic Trigger**:
  - Sends a short pulse to the ultrasonic sensor.
  - Calculates the pulse duration using `pulseIn()`.

- **Distance Calculation**:
  - Converts the duration to distance using the formula:
    \[
    \text{distance\_cm} = \frac{\text{duration\_us} \times 0.0343}{2}
    \]

- **Serial Output**:
  - Logs the current angle and measured distance.
  - Prints "Out of Range" if no echo is detected.

---

### Speaker Beep
```cpp
void beepSpeaker() {
    tone(speakerPin, 1000, 30); 
    delay(10);                  
}
```
- Generates a 1000 Hz sound for 30 ms using the `tone()` function.
- Adds a short delay for stability.

---

## How It Works

1. **Initialization**:
   - Servo motor is attached, pins are set up, and the radar system is initialized.
   
2. **Sweeping Motion**:
   - The servo motor rotates the ultrasonic sensor from 0° to 180° and back.
   
3. **Distance Measurement**:
   - At each angle, the ultrasonic sensor measures the distance to the nearest object and logs it to the serial monitor.
   
4. **Auditory Feedback**:
   - A short beep indicates each distance measurement.

---

## Serial Output Example
```
Radar System Initialized
Angle: 0, Distance: 50.23
Angle: 2, Distance: 48.00
Angle: 4, Distance: Out of Range
...
```

---