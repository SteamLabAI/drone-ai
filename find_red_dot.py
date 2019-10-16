import cv2
import numpy as np

for i in range(10):
    img = cv2.imread("wyjscie" + str(i) + ".jpg")
    img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    mask_red_purple = cv2.inRange(  # For hue values (165, 180)
        img,
        np.array([165, 100, 100]),
        np.array([180, 255, 255])
    )
    mask_red_orange = cv2.inRange(  # For hue values (0, 15)
        img,
        np.array([0, 100, 100]),
        np.array([15, 255, 255])
    )

    mask_red = mask_red_orange + mask_red_purple

    # Blur the mask to ignore image noise and imperfections
    mask_red = cv2.blur(mask_red, (10, 10))

    # Discard values lower than 125
    _, threshed = cv2.threshold(mask, 125, 255, cv2.THRESH_BINARY)

    cv2.imwrite("kropki" + str(i) + ".jpg", threshed)
