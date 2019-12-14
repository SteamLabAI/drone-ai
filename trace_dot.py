import cv2

from util import Recognizer

def get_white_center(img):
    all_white = cv2.countNonZero(img)
    if all_white > 100:
        M = cv2.moments(img)
 
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])
        return (True, cX, cY)
    else:
        return (False, -1, -1)

def main():
    cap = cv2.VideoCapture(1)
    rec = Recognizer()

    while True:
        _, frame = cap.read()
        threshed = rec.recognize_frame(frame)
        result, cX, cY = get_white_center(threshed)

        threshed = cv2.cvtColor(threshed, cv2.COLOR_GRAY2BGR)

        h, w = threshed.shape[0], threshed.shape[1]

        x1, y1, x2, y2 = int(w*0.33), int(h*0.33), int(w*0.66), int(h*0.66)

        if x1 <= cX <= x2 and y1 <= cY <= y2:
            print(True)
        else:
            print(False)

        cv2.rectangle(threshed, (x1, y1), (x2, y2), (0, 255, 255), 5)

        if result:
            cv2.circle(threshed, (cX, cY), 10, (0, 0, 255), -1)

        cv2.imshow('Obraz', threshed)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()