import cv2
import numpy as np
import os

def load_image(image_path):
    """
    Load an image from the specified file path.
    """
    image = cv2.imread(image_path)
    return image

def analyze_image(image):
    """
    Analyze the image to classify it as black, transparent, or colorful.
    Uses brightness and color detection heuristics.
    """
    # Convert to HSV color space for better color/brightness detection
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Calculate average brightness (Value channel)
    brightness = np.mean(hsv[:, :, 2])

    # Calculate saturation mean to help distinguish colorful vs. transparent
    saturation = np.mean(hsv[:, :, 1])

    # Threshold logic:
    if brightness > 180 and saturation < 40:
        # High brightness + low saturation means likely transparent plastic
        return 'transparent'
    elif brightness < 50:
        # Low brightness means black plastic
        return 'black'
    else:
        # Otherwise, colorful plastic (has moderate brightness and saturation)
        return 'colorful'

def assign_belt(category):
    """
    Map the detected category to a conveyor belt.
    """
    belt_map = {
        'black': 'A',
        'transparent': 'B',
        'colorful': 'C'
    }
    return belt_map.get(category, 'Unknown')

def main():
    categories = ['black', 'transparent', 'colorful']

    print("Starting object classification and conveyor belt assignment...\n")

    for category in categories:
        folder_path = category
        if not os.path.exists(folder_path):
            print(f"Folder '{folder_path}' does not exist. Please create it and add images.")
            continue

        image_files = os.listdir(folder_path)
        if len(image_files) == 0:
            print(f"No images found in folder '{folder_path}'. Please add images.")
            continue

        for filename in image_files:
            image_path = os.path.join(folder_path, filename)

            image = load_image(image_path)
            if image is None:
                print(f"Failed to load image: {image_path}")
                continue

            detected_category = analyze_image(image)
            belt = assign_belt(detected_category)

            print(f"Image: {image_path}")
            print(f" - Detected category: {detected_category}")
            print(f" - Send to conveyor belt: {belt}\n")

if __name__ == "__main__":
    main()
