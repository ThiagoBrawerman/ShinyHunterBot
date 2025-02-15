"""
    Description: This module is used to detect objects in an image
    
"""

import cv2  # type: ignore
import numpy as np  # type: ignore


def detect_object(base_img, object_img, threshold: float) -> list:
    """
    Detect the object in the frame
    :param frame: The frame to detect the object in
    :param object_img: The object image to detect
    :param threshold: The threshold value
    :return: The rectangles
    """

    # Get the object image dimensions
    object_height, object_width = object_img.shape[:2]

    # Convert both images to grayscale if they are not already
    if len(base_img.shape) >= 3:
        frame_gray = cv2.cvtColor(base_img, cv2.COLOR_BGR2GRAY)
    else:
        frame_gray = base_img

    if len(object_img.shape) >= 3:
        object_img_gray = cv2.cvtColor(object_img, cv2.COLOR_BGR2GRAY)
    else:
        object_img_gray = object_img

    # Perform template matching
    result = cv2.matchTemplate(frame_gray, object_img_gray, cv2.TM_CCOEFF_NORMED)

    # Get the locations where the threshold is met
    yloc, xloc = np.where(result >= threshold)

    # Create a list to store the rectangles
    rectangles = []

    # Create rectangles for the detected objects
    for x, y in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(object_width), int(object_height)])
        rectangles.append([int(x), int(y), int(object_width), int(object_height)])

    # Group the rectangles
    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    return rectangles
