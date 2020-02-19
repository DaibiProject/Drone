import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #Wanted color
    low_c = np.array([161, 155, 84])
    high_c = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low_c, high_c)
    
    low_d = np.array([240, 100, 50])
    high_d = np.array([240, 100, 80])
    mask2 = cv2.inRange(hsv_frame, low_d, high_d)
    
    cv2.imshow("Frame", frame)
    cv2.imshow("Frame2", mask)
    cv2.imshow("Frame3", mask2)

    key = cv2.waitKey(1)
    if key == 27:
        break
