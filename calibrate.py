import cv2
import numpy as np

cap = cv2.VideoCapture(1)

value_min = 50
value_max = 200
saturation_min = 200
saturation_max = 255
step = 10

white_max = 0
max_params = [0, 255, 0, 255]

ret, frame = cap.read()
img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
cap.release()

for value_lower in range(value_min, value_max + 1, step):
    print(str(value_lower) + "/" + str(value_max))
    for value_upper in range(value_lower, value_max + 1, step):
        for saturation_lower in range(saturation_min, saturation_max + 1, step):
            for saturation_upper in range(saturation_lower, saturation_max + 1, step):
                mask_red_purple = cv2.inRange(  # For hue values (170, 180)
                    img,
                    np.array([177, saturation_lower, value_lower]),
                    np.array([180, saturation_upper, value_upper])
                )
                mask_red_orange = cv2.inRange(  # For hue values (0, 10)
                    img,
                    np.array([0, saturation_lower, value_lower]),
                    np.array([17, saturation_upper, value_upper])
                )

                mask_red = mask_red_orange + mask_red_purple

                # Blur the mask to ignore image noise and imperfections
                mask_red = cv2.blur(mask_red, (25, 25))

                # Discard values lower than 125
                _, threshed = cv2.threshold(
                    mask_red, 125, 255, cv2.THRESH_BINARY)
                white = cv2.countNonZero(threshed)
                if white > white_max:
                    white_max = white
                    max_params = [saturation_lower,
                                  saturation_upper, value_lower, value_upper]

f = open('params.txt', 'w')
f.write(' '.join(list(map(str, max_params))))
f.close()
