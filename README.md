# ESP32 Radar System with Ultrasonic Sensor and Servo Motor

## **Overview**

This project implements a radar-like system using an **ESP32 microcontroller**, an ultrasonic sensor, a servo motor, and a speaker. The servo motor sweeps the ultrasonic sensor across a range of angles, measuring distances and displaying them on the serial monitor. A speaker provides auditory feedback for each measurement.

---

## **Components Used**

1. **Ultrasonic Sensor (HC-SR04)**
   - Emits ultrasonic waves to measure distances based on the echo return time.

2. **Servo Motor**
   - Rotates the ultrasonic sensor, enabling a sweeping motion (0° to 180°).

3. **Speaker (Buzzer)**
   - Emits a beep for each distance measurement.

4. **ESP32 Board**
   - Controls the components and processes the logic.

---

## **Pin Connections**

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

## **Arduino Code Overview**

The Arduino code controls the radar system by:

- Initializing the servo motor, ultrasonic sensor, and speaker.
- Moving the servo from 0° to 180° and back in 2° increments.
- Measuring the distance to nearby objects using the ultrasonic sensor at each angle.
- Logging the measured distance and angle to the serial monitor.
- Providing auditory feedback through the speaker for each measurement.

---

## **Python Visualization Script**

A Python script is included to visualize the radar data using a graphical radar display. The script connects to the ESP32 via a serial port and creates a 180-degree radar visualization using **Pygame**.

### Key Features:

1. **Serial Data Reading**:
   - Reads angle and distance data from the ESP32 via the specified serial port.
   - Filters out-of-range data for a cleaner display.

2. **Graphical Radar Display**:
   - Displays a sweeping radar with a half-circle grid.
   - Plots detected objects as red dots based on their angle and distance.
   - Includes a dynamic sweeping line to simulate radar motion.

3. **Concurrency**:
   - Uses threading to read data and update the display simultaneously.

### Python Script Highlights:

- **Dependencies**: Ensure `pygame` and `pyserial` are installed using:
  ```bash
  pip install pygame pyserial
  ```

- **Execution**: Update the serial port in the script (e.g., `COM5`) and run:
  ```bash
  python radar_display.py
  ```

- **Code Example**:

  ```python
  for angle, distance in read_serial_data(port):
      if 0 <= distance <= max_distance:
          radar_data.append((angle, distance))
  ```

---

## **How It Works**

1. **Initialization**:
   - The radar system initializes the servo motor, ultrasonic sensor, and speaker.

2. **Sweeping Motion**:
   - The servo motor rotates the ultrasonic sensor between 0° and 180°, scanning for objects.

3. **Distance Measurement**:
   - At each angle, the ultrasonic sensor measures the distance to nearby objects and logs it to the serial monitor.

4. **Visualization**:
   - The Python script visualizes the radar data in real time on a Pygame display.

---

## 🖥**Serial Output Example**

```
Radar System Initialized
Angle: 0, Distance: 50.23
Angle: 2, Distance: 48.00
Angle: 4, Distance: Out of Range
...
```

---

## **Repository Content**

- **`radar.ino`**: Arduino sketch for the radar system.
- **`radar.py`**: Python script for visualizing radar data.
- **`README.md`**: Project documentation.

---

## **Demo**

Will look similar to this Demo done by [Coders Cafe](https://www.youtube.com/@CodersCafeTech/shorts).

The Demo: ![Radar System Demo](https://www.youtube.com/shorts/o7DMHJKhpws)!

---

## **License**

This project is licensed under the MIT License. See `LICENSE` for details.

---

## **Contact**

For questions or suggestions, reach out at [mail@tgm.ac.at](mailto:mail@tgm.ac.at).
