import cv2
import numpy as np


class Recognizer:
    def __init__(self):
        f = open('params.txt', 'r')
        self.params = list(map(int, f.read().split()))

    def recognize_frame(self, frame):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask_red_purple = cv2.inRange(  # For hue values (170, 180)
            img,
            np.array([177, self.params[0], self.params[2]]),
            np.array([180, self.params[1], self.params[3]])
        )
        mask_red_orange = cv2.inRange(  # For hue values (0, 10)
            img,
            np.array([0, self.params[0], self.params[2]]),
            np.array([17, self.params[1], self.params[3]])
        )

        mask_red = mask_red_orange + mask_red_purple

        # Blur the mask to ignore image noise and imperfections
        mask_red = cv2.blur(mask_red, (25, 25))

        # Discard values lower than 125
        _, threshed = cv2.threshold(mask_red, 125, 255, cv2.THRESH_BINARY)
        return threshed
