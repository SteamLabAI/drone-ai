import cv2

from util import Recognizer

rec = Recognizer()

for i in range(10):
    img = cv2.imread('wyjscie' + str(i) + '.jpg')

    threshed = rec.recognize_frame(img)

    cv2.imwrite('kropki' + str(i) + '.jpg', threshed)
