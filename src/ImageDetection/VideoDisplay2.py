"""_summary_
"""

import cv2  # Import the OpenCV library
import numpy as np  # Import the NumPy library
from ImageDetection import detect_object
from VideoDisplay import display_fps, object_display

IMGS_DIRECTORY = "src/ImageDetection/Images"
MainMenuImg = "MainMenu.png"
SettingsMenuImg = "SettingsMenu.png"

Main_path = IMGS_DIRECTORY + "/" + MainMenuImg
Settings_path = IMGS_DIRECTORY + "/" + SettingsMenuImg

main_img = cv2.imread(Main_path, cv2.IMREAD_UNCHANGED)
settings_img = cv2.imread(Settings_path, cv2.IMREAD_UNCHANGED)


cap = cv2.VideoCapture()  # Create a VideoCapture object

# The device number depends on the device and its output
DEVICE_NUMBER = 1  # 1 for the usb of the PC

# Open the video capture device
cap.open(DEVICE_NUMBER, cv2.CAP_DSHOW)


def calculate_fps(prev_frame_time: float, new_frame_time: float) -> float:
    """
    Calculate the frames per second (FPS)
    :param prev_frame_time: The time when the previous frame was processed
    :param new_frame_time: The time when the current frame was processed
    :return: The fps value
    """

    # Calculate the time difference between the current and previous frame
    time_difference = (new_frame_time - prev_frame_time) / cv2.getTickFrequency()

    # Calculate the FPS
    fps = 1 / time_difference if time_difference > 0 else 0

    return fps


# List to store the FPS values
fps_list = []

# The initial tick count
last_tick_count = cv2.getTickCount()

# Loop to read the frames from the video capture device
while cap.isOpened():

    # Read the frame from the video capture device
    ret, img = cap.read()

    object_display(img, detect_object(img, main_img, 0.8))

    # Current tick count
    new_tick_count = cv2.getTickCount()

    # Calculate the FPS and append it to the list
    fps_list.append(calculate_fps(last_tick_count, new_tick_count))

    # Update the last tick count
    last_tick_count = new_tick_count

    # Remove the first element from the list if it exceeds 60 elements
    if len(fps_list) > 60:
        fps_list.pop(0)

    # Calculate the average FPS
    avg_fps = sum(fps_list) / len(fps_list)

    # Display the FPS on the frame
    display_fps(img, avg_fps)

    # Display the frame
    cv2.imshow("frame", img)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break

cap.release()  # Release the video capture device
cv2.destroyAllWindows()  # Close the window
