import cv2
import numpy as np

for i in range(10):
    img = cv2.imread("wyjscie" + str(i) + ".jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 50, 50])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(img, lower_red, upper_red)
    mask = cv2.blur(mask, (20, 20))

    th, threshed = cv2.threshold(
        mask, 200, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    cv2.imwrite("kropki" + str(i) + ".jpg", threshed)
