import cv2  # type: ignore


from VideoProcessing import (
    calculate_fps,
    display_fps,
    display_object,
    generate_img_list,
    update_img_detected_list,
)

# The directory of the images
IMGS_DIRECTORY = "src/ImageDetection/Images"

# The device number depends on the device and its output
DEVICE_NUMBER = 1  # 1 for the usb of the PC

# Can Display the images?
CAN_DISPLAY = True

# Color palette
COLORS = [
    (1, 190, 254),
    (255, 221, 0),
    (255, 125, 0),
    (255, 0, 109),
    (173, 255, 2),
    (143, 0, 255),
]

# Create a VideoCapture object
cap = cv2.VideoCapture()
print(cap)
# Open the video capture device
cap.open(DEVICE_NUMBER, cv2.CAP_DSHOW)
print(cap)

# List to store the FPS values
fps_list = []

# The initial tick count
last_tick_count = cv2.getTickCount()

img_list = generate_img_list(IMGS_DIRECTORY)
detected_list = []

# Loop to read the frames from the video capture device
while cap.isOpened():

    # Read the frame from the video capture device
    ret, img = cap.read()

    # Update the list of the number of detected objects in each image
    detected_list = update_img_detected_list(img_list, img, 0.9)

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

    # If the user wants to display the images
    if CAN_DISPLAY:

        # Display the detected objects on the frame
        for i, val in enumerate(img_list):
            display_object(
                img,
                img_list[i][0],
                detected_list[i],
                (COLORS[i][2], COLORS[i][1], COLORS[i][0]),
            )

        # Display the FPS on the frame
        display_fps(img, avg_fps)

        # Display the frame
        cv2.imshow("frame", img)

    # Break the loop if the user presses the 'q' key
    if cv2.waitKey(2) & 0xFF == ord("q"):
        break
