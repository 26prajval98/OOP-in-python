import cv2
import numpy as np

webcamvideo = cv2.VideoCapture(0)
while True:
    _, frame = webcamvideo.read()

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit = np.array([0, 10, 10])
    upperLimit = np.array([0, 255, 255])

    ref1 = cv2.inRange(img, lowerLimit, upperLimit)

    lowerLimit = np.array([160, 0, 0])
    upperLimit = np.array([180, 255, 255])

    ref2 = cv2.inRange(img, lowerLimit, upperLimit)

    ref = cv2.bitwise_or(ref1, ref2)

    filtered = cv2.bitwise_or(frame, frame, mask=ref)
    smoothImg = cv2.medianBlur(filtered, 55)
    # GaussianBlur
    # bilateralBlur

    # cv2.imshow('ref', ref)
    # cv2.imshow('filtered', filtered)
    cv2.imshow('smooth', smoothImg)
    cv2.imshow('webcam', frame)

    key = cv2.waitKey(33)
    if key == 27 or key == ord('q'):
        break

webcamvideo.release()
cv2.destroyAllWindows()
