import cv2
import numpy as np
import os
from PIL import Image

# Print the current working directory
print("Current working directory:", os.getcwd())

# Construct the absolute path to the image file
image_path = os.path.abspath("heart.png")
print("Absolute path to the image file:", image_path)
image_path = "heart.png"

# Check if the file exists
if not os.path.exists(image_path):
    print("Error: The image file does not exist.")
else:
    print("The image file exists.")

    # Check file permissions
    if os.access(image_path, os.R_OK):
        print("Read permission: Yes")
    else:
        print("Read permission: No")

    if os.access(image_path, os.W_OK):
        print("Write permission: Yes")
    else:
        print("Write permission: No")

    if os.access(image_path, os.X_OK):
        print("Execute permission: Yes")
    else:
        print("Execute permission: No")

    # Try loading the image with OpenCV
    ArceusAppears_img = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if ArceusAppears_img is None:
        print("Error: Could not load image with OpenCV. Check the file path and name.")
    else:
        print("Image loaded successfully with OpenCV.")

    # Try loading the image with PIL
    try:
        pil_image = Image.open(image_path)
        pil_image.verify()  # Verify that it is, in fact, an image
        print("Image loaded successfully with PIL.")
    except (IOError, SyntaxError) as e:
        print("Error: Could not load image with PIL. The file might be corrupted.")
