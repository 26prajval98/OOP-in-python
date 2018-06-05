# Using webcam as image source

import cv2

webcamvideo = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/output.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = webcamvideo.read()

    cv2.imshow('webcam', frame)
    cv2.imshow('grey webcam', cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
    out.write(frame)

    key = cv2.waitKey(33)
    if key == 27 or key == ord('q'):
        break

out.release()
webcamvideo.release()
cv2.destroyAllWindows()