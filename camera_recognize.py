import numpy as np
import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()

    cv2.imshow('Obraz', frame)

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask_red_purple = cv2.inRange(  # For hue values (170, 180)
        img,
        np.array([177, 225, 125]),
        np.array([180, 255, 255])
    )
    mask_red_orange = cv2.inRange(  # For hue values (0, 10)
        img,
        np.array([0, 225, 125]),
        np.array([17, 255, 255])
    )

    mask_red = mask_red_orange + mask_red_purple

    # Blur the mask to ignore image noise and imperfections
    mask_red = cv2.blur(mask_red, (25, 25))

    # Discard values lower than 125
    _, threshed = cv2.threshold(mask_red, 125, 255, cv2.THRESH_BINARY)

    cv2.imshow('Rozpoznanie', threshed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
