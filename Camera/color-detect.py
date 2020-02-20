import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    tickmark=cv2.getTickCount()
    
    #Wanted color
    low_c = np.array([161, 155, 84])
    high_c = np.array([179, 255, 255])
    mask = cv2.inRange(hsv_frame, low_c, high_c)
    
    low_d = np.array([94, 120, 80])
    high_d = np.array([126, 255, 255])
    mask2 = cv2.inRange(hsv_frame, low_d, high_d)
    
    contours, hierarchy = cv2.findContours(mask2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #display Masks
    cv2.imshow("Frame2", mask)
    cv2.imshow("Frame3", mask2)
    
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('video', frame)
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

#should display contour point.

img = np.zeros((512,512,3), np.uint8)

for cnt in contours:
    
    print (cnt[[0]])
    if len(cnt[[0]]) > 0:
        print( cnt[[[0]]], cnt[[[1]]])
        cv2.circle(img, (cnt[[0]][0],cnt[[0]][1]), 10, (0,0,255), -1)

cv2.imshow("test",img)
