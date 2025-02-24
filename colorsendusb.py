import cv2
import numpy as np
import webcolors
import serial  # Import pyserial

# Set up serial communication with Arduino (adjust COM port based on your system)
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's port

def closest_color(requested_color):
    """Finds the closest human-readable color name for an RGB value"""
    color_names = list(webcolors.CSS3_HEX_TO_NAMES.values())  # Get color names
    rgb_values = [webcolors.hex_to_rgb(hex) for hex in webcolors.CSS3_HEX_TO_NAMES.keys()]
    differences = [sum((a - b) ** 2 for a, b in zip(requested_color, rgb)) for rgb in rgb_values]
    return color_names[differences.index(min(differences))]

def detect_color():
    cap = cv2.VideoCapture(0)  # Open the webcam
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Failed to capture image")
        return

    avg_color = frame.mean(axis=0).mean(axis=0)  # Get average color
    color_rgb = (int(avg_color[2]), int(avg_color[1]), int(avg_color[0]))  # Convert BGR to RGB

    # Get closest human-readable color name
    color_name = closest_color(color_rgb)
    print(f"Detected Color: {color_name} | RGB: {color_rgb}")

    # Send RGB values to Arduino
    color_string = f"{color_rgb[0]},{color_rgb[1]},{color_rgb[2]}\n"  # Format: R,G,B
    arduino.write(color_string.encode())  # Send to Arduino

detect_color()
