import serial
import pygame
import math
import threading

def read_serial_data(port, baudrate=9600):
    """
    Reads radar data from a serial port.
    :param port: Serial port (e.g., 'COM5').
    :param baudrate: Communication speed.
    :yield: angle and distance data.
    """
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        print(f"Listening on {port}...")
    except serial.SerialException as e:
        print(f"Failed to open port {port}: {e}")
        return

    try:
        while True:
            line = ser.readline().decode('utf-8').strip()
            if line.startswith("Angle") and "Distance" in line:
                try:
                    angle = float(line.split('Angle: ')[1].split(',')[0])
                    distance = float(line.split('Distance: ')[1])
                    yield angle, distance
                except (IndexError, ValueError):
                    print(f"Failed to parse: {line}")
    except KeyboardInterrupt:
        print("Stopping serial data read...")
    finally:
        ser.close()

def radar_display(port):
    """
    Pygame Radar Display: Visualizes sweeping radar for 180-degree range.
    """
    # Initialize Pygame
    pygame.init()
    screen_width, screen_height = 800, 400  # Half-height screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("180-Degree Radar Display")

    # Radar settings
    center = (screen_width // 2, screen_height)  # Radar origin at bottom-center
    max_distance = 300  # Maximum distance shown on radar
    radar_color = (0, 255, 0)  # Green color for radar elements
    point_color = (255, 0, 0)  # Red color for radar points
    sweep_speed = 2  # Sweep speed (degrees per frame)

    # Shared data for radar points
    radar_data = []
    data_lock = threading.Lock()
    running = True

    # Read serial data in a separate thread
    def data_listener():
        nonlocal running
        for angle, distance in read_serial_data(port):
            print(f"Angle: {angle}, Distance: {distance}")
            with data_lock:
                if 0 <= distance <= max_distance:  # Ignore out-of-range points
                    radar_data.append((angle, distance))
                if len(radar_data) > 50:  # Cap to 50 points
                    radar_data.pop(0)
            if not running:
                break

    # Start the data listener thread
    listener_thread = threading.Thread(target=data_listener, daemon=True)
    listener_thread.start()

    # Radar sweep angle
    current_angle = 0
    sweep_direction = 1  # 1 for increasing angle, -1 for decreasing angle

    # Main Pygame loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw radar grid (half-circle)
        for r in range(50, max_distance + 1, 50):  # Concentric arcs
            pygame.draw.arc(screen, radar_color,
                            (center[0] - r, center[1] - r, 2 * r, 2 * r),
                            math.pi, 2 * math.pi, 1)

        for angle in range(0, 181, 30):  # Radial lines every 30 degrees
            x = center[0] + int(max_distance * math.cos(math.radians(180 - angle)))
            y = center[1] - int(max_distance * math.sin(math.radians(180 - angle)))
            pygame.draw.line(screen, radar_color, center, (x, y), 1)

        # Draw sweeping line
        sweep_x = center[0] + int(max_distance * math.cos(math.radians(180 - current_angle)))
        sweep_y = center[1] - int(max_distance * math.sin(math.radians(180 - current_angle)))
        pygame.draw.line(screen, radar_color, center, (sweep_x, sweep_y), 2)

        # Draw radar points
        with data_lock:
            for angle, distance in radar_data:
                x = center[0] + int(distance * math.cos(math.radians(180 - angle)))
                y = center[1] - int(distance * math.sin(math.radians(180 - angle)))
                pygame.draw.circle(screen, point_color, (x, y), 5)

        # Update the radar sweep
        current_angle += sweep_direction * sweep_speed
        if current_angle >= 180 or current_angle <= 0:
            sweep_direction *= -1  # Reverse sweep direction

        # Refresh screen
        pygame.display.flip()
        pygame.time.delay(30)

    # Clean up
    pygame.quit()
    print("Radar display stopped.")

if __name__ == "__main__":
    try:
        port = "COM5"  # Replace with your serial port
        radar_display(port)
    except Exception as e:
        print(f"Error: {e}")
