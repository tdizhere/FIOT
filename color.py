import cv2
import numpy as np
import webcolors
from scipy.spatial import KDTree

def get_color_name(requested_color):
    """Finds the closest human-readable color name for an RGB value."""
    # Define a dictionary of color names and their corresponding RGB values
    color_names = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'cyan': (0, 255, 255),
        'magenta': (255, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'gray': (128, 128, 128),
        'orange': (255, 165, 0),
        'purple': (128, 0, 128),
        'pink': (255, 192, 203),
        # Add more colors as needed
    }
    
    # Create a KDTree for fast nearest-neighbor lookup
    color_tree = KDTree(list(color_names.values()))
    _, index = color_tree.query(requested_color)
    closest_color_name = list(color_names.keys())[index]
    return closest_color_name

def detect_color():
    cap = cv2.VideoCapture(0)  # Open the webcam
    ret, frame = cap.read()
    cap.release()
    
    if not ret:
        print("Failed to capture image")
        return

    avg_color = frame.mean(axis=0).mean(axis=0)  # Get average color
    color_rgb = (int(avg_color[2]), int(avg_color[1]), int(avg_color[0]))  # Convert BGR to RGB
    print("Detected Color (RGB):", color_rgb)

    # Get the closest color name
    color_name = get_color_name(color_rgb)
    print("Detected Color Name:", color_name)

    return color_rgb, color_name

detect_color()
