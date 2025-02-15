from ImageDetection import detect_object
from Display import display_object, display_fps

import cv2  # type: ignore
from os import listdir
from os.path import isfile, join


# Function to calculate the frames per second (FPS)
def calculate_fps(prev_frame_time: float, new_frame_time: float):
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


# Function to generate a list of tuples of the images name and the images
def generate_img_list(images_directory: str) -> list:
    """
    Generate a list of images
    :param imgs_directory: The directory of the images
    :return: The list of images
    """

    # Create a list to store the images
    image_list = []

    # Create a list to store the images file name
    image_file_name_list = []

    # Get the list of the images file name
    for file in listdir(images_directory):

        # Get the file path
        path = join(images_directory, file)

        # Check if the file is an image file
        if isfile(path) and (file.endswith(".png") or file.endswith(".jpg")):

            # Store the image file name
            image_file_name_list.append(file)

    # Loop through the images
    for image_file_name in image_file_name_list:

        # Get the image real name
        image_name = image_file_name.split(".")[0]

        # Read the image
        image = cv2.imread(
            images_directory + "/" + image_file_name, cv2.IMREAD_UNCHANGED
        )

        image_list.append([image_name, image])

    return image_list


# Function to update the list of the number of detected objects in the images
def update_img_detected_list(
    image_list: list, image_base: list, threshold: float
) -> list:
    """
    Update the list of the number of detected objects in each image
    :param image_list: The list of images
    :param image_base: The base image
    :param threshold: The threshold value
    :return: The updated list of the number of detected objects in each image

    obs.: This function is very slow
    """
    # Check if the threshold value is between 0 and 1
    if threshold < 0 or threshold > 1:
        raise ValueError("The threshold value must be between 0 and 1")

    image_detected_list = []
    # Loop through the images

    for image in image_list:

        # Detect the objects in the image
        detected_objects = detect_object(image_base, image[1], threshold)

        # Append the number of detected objects to the list
        image_detected_list.append(detected_objects)

    return image_detected_list
