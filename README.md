# ESP32 Radar System with Ultrasonic Sensor and Servo Motor

## 🌟 **Overview**

This project implements a radar-like system using an **ESP32 microcontroller**, an ultrasonic sensor, a servo motor, and a speaker. The servo motor sweeps the ultrasonic sensor across a range of angles, measuring distances and displaying them on the serial monitor. A speaker provides auditory feedback for each measurement.

---

## 🛠️ **Components Used**

1. **Ultrasonic Sensor (HC-SR04)**
   - Emits ultrasonic waves to measure distances based on the echo return time.

2. **Servo Motor**
   - Rotates the ultrasonic sensor, enabling a sweeping motion (0° to 180°).

3. **Speaker (Buzzer)**
   - Emits a beep for each distance measurement.

4. **ESP32 Board**
   - Controls the components and processes the logic.

---

## 🔌 **Pin Connections**

| Component         | ESP32 Pin     |
|--------------------|---------------|
| Ultrasonic Trig    | GPIO 9        |
| Ultrasonic Echo    | GPIO 8 (via Voltage Divider) |
| Servo Signal       | GPIO 10       |
| Speaker Positive   | GPIO 3        |

> **Note:** Use a voltage divider with 10kΩ and 20kΩ resistors to step down the ultrasonic sensor’s Echo pin output from 5V to 3.3V to protect the ESP32.

---

## 📐 **Circuit Diagram**

Below is the circuit diagram for connecting the components:

![Circuit Diagram](https://github.com/user-attachments/assets/3b42a63d-4cbc-460d-ba6d-096025b44e29)

> **Tip:** Use an external 5V power supply for the servo motor to avoid overloading the ESP32’s power regulator.

---

## 📜 **Code Breakdown**

### 🚀 Libraries Used

```cpp
#include <Servo.h>
```
- The `Servo` library is used to control the servo motor's rotation.

### 📋 Global Variables

1. **Pins**:
   - Define pins for ultrasonic sensor (`trigPin`, `echoPin`), servo motor (`servoPin`), and speaker (`speakerPin`).

2. **Servo Object**:
   - `Servo myServo` creates an instance for servo motor control.

3. **Distance Variables**:
   - `duration_us`: Time for echo return.
   - `distance_cm`: Distance to the object in centimeters.

4. **Angle**:
   - `angle`: Tracks the servo motor’s current position.

### 🛠️ Setup Function

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
- Initializes components and sets up serial communication.

### 🔄 Main Loop

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
- Moves the servo from 0° to 180° and back in 2° increments, measuring distances at each position.

### 📏 Distance Measurement

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
- Sends a pulse, measures echo time, and calculates distance.

### 🎵 Speaker Beep

```cpp
void beepSpeaker() {
    tone(speakerPin, 1000, 30);
    delay(10);
}
```
- Emits a 1000 Hz sound for 30 ms.

---

## 🎯 **How It Works**

1. **Initialization**:
   - The radar system initializes the servo motor, ultrasonic sensor, and speaker.

2. **Sweeping Motion**:
   - The servo motor rotates the ultrasonic sensor between 0° and 180°, scanning for objects.

3. **Distance Measurement**:
   - At each angle, the ultrasonic sensor measures the distance to nearby objects and logs it to the serial monitor.

4. **Auditory Feedback**:
   - A beep sound provides auditory feedback for each measurement.

---

## 🖥️ **Serial Output Example**

```
Radar System Initialized
Angle: 0, Distance: 50.23
Angle: 2, Distance: 48.00
Angle: 4, Distance: Out of Range
...
```

---

## 📦 **Repository Content**

- **`main.ino`**: Arduino sketch for the radar system.
- **`CircuitDiagram.png`**: Visual representation of the connections.
- **`README.md`**: Project documentation.

---

## 📸 **Demo**

Will look similar to this Demo done by [Coders Cafe](https://www.youtube.com/@CodersCafeTech/shorts)
![Radar System Demo](https://www.youtube.com/shorts/o7DMHJKhpws)

---

## 📜 **License**

This project is licensed under the MIT License. See `LICENSE` for details.

---

## 🌐 **Contact**

For questions or suggestions, reach out at [mail@tgm.ac.at](mailto:mail@tgm.ac.at).
