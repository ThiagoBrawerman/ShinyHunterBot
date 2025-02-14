import cv2
import numpy as np
import os
import time

# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0

IMGS_DIRECTORY = "src/ImageDetection/Images"
MainMenuImg = "MainMenu.png"

Main_path = os.path.join(IMGS_DIRECTORY, MainMenuImg)

# Check if the image file exists
if not os.path.exists(Main_path):
    print(f"Error: The image file {Main_path} does not exist.")
else:
    main_img = cv2.imread(Main_path, cv2.IMREAD_UNCHANGED)
    if main_img is None:
        print(f"Error: Could not load image {Main_path}.")
    else:
        width = main_img.shape[1]
        height = main_img.shape[0]

        threshold = 0.8

        cap = cv2.VideoCapture()
        # The device number might be 0 or 1 depending on the device and the webcam
        if not cap.open(1, cv2.CAP_DSHOW):
            print("Error: Could not open video capture device.")
        else:
            while True:

                ret, frame = cap.read()
                if not ret:
                    print("Error: Could not read frame from video capture device.")
                    break

                # Our operations on the frame come here
                gray = frame

                # resizing the frame size according to our need
                gray = cv2.resize(gray, (500, 300))

                # font which we will be using to display FPS
                font = cv2.FONT_HERSHEY_SIMPLEX
                # time when we finish processing for this frame
                new_frame_time = time.time()

                # Calculating the fps

                # fps will be number of frame processed in given time frame
                # since their will be most of time error of 0.001 second
                # we will be subtracting it to get more accurate result
                fps = 1 / (new_frame_time - prev_frame_time)
                prev_frame_time = new_frame_time

                # converting the fps into integer
                fps = int(fps)

                # converting the fps to string so that we can display it on frame
                # by using putText function
                fps = str(fps)

                # putting the FPS count on the frame
                cv2.putText(gray, fps, (7, 70), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

                result = cv2.matchTemplate(main_img, frame, cv2.TM_CCOEFF_NORMED)
                yloc, xloc = np.where(result >= threshold)

                rectangles = []
                for x, y in zip(xloc, yloc):
                    rectangles.append([int(x), int(y), int(width), int(height)])
                    rectangles.append([int(x), int(y), int(width), int(height)])

                rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

                for x, y, w, h in rectangles:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                cv2.imshow("frame", gray)
                if cv2.waitKey(2) & 0xFF == ord("q"):
                    break

            cap.release()
            cv2.destroyAllWindows()
