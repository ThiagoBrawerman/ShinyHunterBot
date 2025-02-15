"""
This module contains the functions to display the frames per second (FPS)
and the detected object on the frame.
"""

# Import the OpenCV library
import cv2  # type: ignore


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

    # Calculate the coordinate of the text (center of the rectangle)
    text_x = (
        rect_top_left[0] + (rect_bottom_right[0] - rect_top_left[0] - text_size[0]) // 2
    )
    text_y = (
        rect_top_left[1] + (rect_bottom_right[1] - rect_top_left[1] + text_size[1]) // 2
    )

    # Write the border text on the frame
    cv2.putText(
        frame,
        fps_text,
        (text_x, text_y),
        font,
        font_scale,
        (0, 0, 0),
        3,
        cv2.LINE_AA,
    )

    # Write text on the frame
    cv2.putText(
        frame,
        fps_text,
        (text_x, text_y),
        font,
        font_scale,
        (255, 255, 255),
        1,
        cv2.LINE_AA,
    )
    # Give thickness to the text
    cv2.putText(
        frame,
        fps_text,
        (text_x + 1, text_y),
        font,
        font_scale,
        (255, 255, 255),
        1,
        cv2.LINE_AA,
    )


def display_object(frame, title: str, rectangles, color: tuple):
    """
    Display the object on the frame
    :param frame: The frame to display the object on
    :param title: The title of the object
    :param rectangles: The rectangles to display
    :param color: The color of the rectangles
    """
    # Get the number of characters in the title
    title_size = len(title)

    # Define the rectangle width and height
    rectangle_width = 100
    rectangle_height = 20

    # Truncate the title if it is too long
    if title_size > 10:
        title = title[:7] + "..."

    # Font which we will be using to display FPS
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Set the font scale
    font_scale = 0.55

    # Get the text size
    text_size = cv2.getTextSize(title, font, font_scale, 2)[0]

    # Draw the rectangles on the frame
    for x, y, w, h in rectangles:

        # Define the rectangle's top-left and bottom-right corners
        rect_top_left = (x + w - rectangle_width, y)
        rect_bottom_right = (x + w, y - rectangle_height)

        # Calculate the coordinate of the text
        text_x = (
            rect_top_left[0]
            + (rect_bottom_right[0] - rect_top_left[0] - text_size[0]) // 2
        )
        text_y = (
            rect_top_left[1]
            + (rect_bottom_right[1] - rect_top_left[1] + text_size[1]) // 2
        )

        # Draw the rectangles on the frame
        cv2.rectangle(
            frame, rect_top_left, rect_bottom_right, color, 2
        )  # Perimeter of the object

        cv2.rectangle(
            frame, rect_top_left, rect_bottom_right, color, -1
        )  # Object title frame
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)  # Object title perimeter

        # Display the border of the title
        cv2.putText(
            frame,
            title,
            (text_x, text_y),
            font,
            font_scale,
            (0, 0, 0),
            3,
            cv2.LINE_AA,
        )
        # Display the title of the object
        cv2.putText(
            frame,
            title,
            (text_x, text_y),
            font,
            font_scale,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )
        # Give the title thickness

        cv2.putText(
            frame,
            title,
            (text_x + 1, text_y),
            font,
            font_scale,
            (255, 255, 255),
            1,
            cv2.LINE_AA,
        )
