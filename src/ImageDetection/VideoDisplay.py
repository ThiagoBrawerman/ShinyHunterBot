"""
This module contains the functions to display the frames per second (FPS) and the detected object on the frame.
"""

import cv2  # Import the OpenCV library


def display_fps(frame, fps: int):
    """
    Display the frames per second (FPS) on the frame
    :param frame: The frame to display the FPS on
    :param fps: The FPS value to display
    """

    # Draw the display rectangles

    # Get frame dimensions
    frame_height, frame_width = frame.shape[:2]

    # Define the rectangle width and height
    rectangle_width = 80
    rectangle_height = 30

    # Define the rectangle's top-left and bottom-right corners
    rect_top_left = (frame_width - rectangle_width, 0)
    rect_bottom_right = (frame_width, rectangle_height)

    # Define the border's top-left and bottom-right corners
    border_top_left = (0, 0)
    border_bottom_right = (frame_width, frame_height)

    # Draw the rectangles on the frame
    cv2.rectangle(
        frame, rect_top_left, rect_bottom_right, (0, 255, 0), -1
    )  # FPS rectangle
    cv2.rectangle(
        frame, border_top_left, border_bottom_right, (0, 255, 0), 5
    )  # Border rectangle

    # Define the text to display

    # Font which we will be using to display FPS
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Set the font scale
    font_scale = 0.55

    # Adding the FPS to the frame
    # Convert the FPS to a string
    fps_text = f"FPS: {int(fps)}"

    # Get the text size
    text_size = cv2.getTextSize(fps_text, font, font_scale, 2)[0]

    # Calculate the coordinate of the text
    text_x = (
        rect_top_left[0] + (rect_bottom_right[0] - rect_top_left[0] - text_size[0]) // 2
    )
    text_y = (
        rect_top_left[1] + (rect_bottom_right[1] - rect_top_left[1] + text_size[1]) // 2
    )

    cv2.putText(
        frame,
        fps_text,
        (text_x, text_y),
        font,
        font_scale,
        (255, 255, 255),
        2,
        cv2.LINE_AA,
    )


def object_display(frame, rectangles):
    """
    Display the object on the frame
    :param frame: The frame to display the object on
    :param rectangles: The rectangles to display
    """

    # Draw the rectangles on the frame
    for x, y, w, h in rectangles:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 2)
