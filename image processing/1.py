import numpy as np
import cv2

webcamvideo = cv2.VideoCapture(0)

while True:
    ret, frame = webcamvideo.read()

    cv2.imshow('webcam', frame)
    cv2.imshow('grey webcam', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))

    key = cv2.waitKey(33)
    if key == 27 or key == ord('q'):
        break

webcamvideo.release()
cv2.destroyAllWindows()