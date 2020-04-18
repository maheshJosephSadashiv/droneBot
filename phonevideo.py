import cv2 
import numpy as np
url = 'http://192.168.2.26:8600/video'
cap = cv2.VideoCapture(url)
while(True):
    ret, frame = cap.read()
    if frame is not None:
        frame = cv2.resize(frame, (600,400), interpolation = cv2.INTER_AREA)
        cv2.imshow('frame',frame)
    q = cv2.waitKey(1)
    if q == ord("q"):
        break
cv2.destroyAllWindows()
