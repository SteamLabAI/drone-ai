import cv2

from util import Recognizer

cap = cv2.VideoCapture(1)

rec = Recognizer()

while True:
    ret, frame = cap.read()

    cv2.imshow('Obraz', frame)

    threshed = rec.recognize_frame(frame)

    cv2.imshow('Rozpoznanie', threshed)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
