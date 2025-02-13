import cv2
import numpy as np


IMGS_DIRECTORY = "src/ImageDetection/Images"
MainMenuImg = "MainMenu.png"
SettingsMenuImg = "SettingsMenu.png"

Main_path = IMGS_DIRECTORY + "/" + MainMenuImg
Settings_path = IMGS_DIRECTORY + "/" + SettingsMenuImg

main_img = cv2.imread(Main_path, cv2.IMREAD_UNCHANGED)
settings_img = cv2.imread(Settings_path, cv2.IMREAD_UNCHANGED)

cv2.imshow("Main Menu Image", main_img)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imshow("Settings Menu Image", settings_img)
cv2.waitKey()
cv2.destroyAllWindows()

result = cv2.matchTemplate(main_img, settings_img, cv2.TM_CCOEFF_NORMED)

cv2.imshow("Result", result)
cv2.waitKey()
cv2.destroyAllWindows()

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

print(max_val, max_loc)

width = settings_img.shape[1]
height = settings_img.shape[0]


threshold = 0.32

yloc, xloc = np.where(result >= threshold)

print(len(xloc))

rectangles = []
for x, y in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(width), int(height)])
    rectangles.append([int(x), int(y), int(width), int(height)])

print(len(rectangles))

rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

print(len(rectangles))

for x, y, w, h in rectangles:
    cv2.rectangle(main_img, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Main Menu Image", main_img)
cv2.waitKey()
cv2.destroyAllWindows()
