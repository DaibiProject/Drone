import cv2
import numpy as np
import math
from math import sqrt

cap = cv2.VideoCapture(0)
a = 0

i = 0

moy = 0

tab = [0.0,0.0,0.0,0.0,0.0]
ouv = math.tan(48.5/2)
jj = 0

xx = 0

xy = []
gr1 = []
gr2 = []

centre = [0,0]

while True:

    #Key
    key = cv2.waitKey(1)
    if key == 27:
        break

    
    #Video reading and conversion to HSV
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #cv2.circle(frame, (200,200), 3, (255,255,255),3)
    #print(hsv_frame[200,200])

    #First part of FPS display
    tickmark=cv2.getTickCount()
    
    #Wanted color (HSV form)
    low_d = np.array([94, 80, 2])
    high_d = np.array([126, 255, 255])
    mask2 = cv2.inRange(hsv_frame, low_d, high_d)

    #Thresh maks... (needed) 
    ret, thresh = cv2.threshold(mask2, 200, 255, 0)

    #Contour finding and display
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    biggest_contours = sorted(contours, key=cv2.contourArea)[-3:]   
    if a==1 or a==2:
        try:
            cv2.drawContours(frame, biggest_contours, -1, (0,255,0), 3)
        except cv2.error:
            print ("err")

    
    #Just for debug - contour point (one point per contour)
    if key == 97:
        if a == 0:
            a = 1
        elif a == 1:
            a = 2
        elif a == 2:
            a = 0
        print(a)

    img = np.zeros((500,700,3), np.uint8)
    if a == 2:
        for cnt in contours:
            if len(cnt[0][0]) > 1:
                x = int(cnt[0][0][0])
                y = int(cnt[0][0][1])
                cv2.circle(img, (x,y), 1, (0,0,255), 2)

                cv2.imshow("test",img)
                
            
    for b_cnt in biggest_contours:
        approx = cv2.approxPolyDP(b_cnt, .03 * cv2.arcLength(b_cnt, True), True)

        if len(approx) == 8:
            area = cv2.contourArea(b_cnt)
            (cx, cy), radius = cv2.minEnclosingCircle(b_cnt)
            cv2.circle(frame, (int(cx),int(cy)), int(radius), (0,0,150), -1)
            circleArea = radius * radius * np.pi
            
            if round(circleArea) > (round(area)-(radius * 20)) and round(circleArea) < (round(area)+(radius * 20)):
                #cv2.drawContours(frame, [b_cnt], 0, (0, 0, 255), -1)
                cv2.circle(frame, (int(cx),int(cy)), int(radius), (150,0,150), 3)
                e = (1280/(2*ouv))
               

                f = (sqrt((640-cx)*(640-cx)+(360-cy)*(360*cy)))
                
                r = sqrt(e*e+f*f)
                r = r * 4.3/(radius*2)

                print(e,f,r)
                    

                    


                

                  
            
                



    
    #Display Masks
    cv2.imshow("Frame3", mask2)
  

    
    #Second part of FPS display
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(frame, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow('video', frame)




cap.release()
cv2.destroyAllWindows()

#Display the last contour point
for cnt in contours:
    
    if len(cnt[0][0]) > 1:
        x = int(cnt[0][0][0])
        y = int(cnt[0][0][1])
        cv2.circle(img, (x,y), 1, (0,0,255), 2)
        cv2.imshow("test",img)

cv2.imshow("test",img)
