import cv2
import numpy as np
import math
from math import sqrt
#import smbus

#Variable statement 
cap = cv2.VideoCapture(0)
a = 0
moy = 0
tab = [0.0,0.0,0.0,0.0,0.0]
ouv = math.tan(48.5/2)


while True:

    #Key
    key = cv2.waitKey(1)
    if key == 27:
        break

    
    #Video reading and conversion to HSV
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
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

    #contour
    img = np.zeros((500,700,3), np.uint8)
    if a == 2:
        for cnt in contours:
            if len(cnt[0][0]) > 1:
                x = int(cnt[0][0][0])
                y = int(cnt[0][0][1])
                cv2.circle(img, (x,y), 1, (0,0,255), 2)

                cv2.imshow("test",img)
                
    #biggest contour    
    for b_cnt in biggest_contours:
        approx = cv2.approxPolyDP(b_cnt, .03 * cv2.arcLength(b_cnt, True), True)

        #if looks like circle
        if len(approx) == 8:
            area = cv2.contourArea(b_cnt)
            (cx, cy), radius = cv2.minEnclosingCircle(b_cnt)
            cv2.circle(frame, (int(cx),int(cy)), int(radius), (0,0,150), -1)
            circleArea = radius * radius * np.pi

            #then compare to a circle area
            if round(circleArea) > (round(area)-(radius * 20)) and round(circleArea) < (round(area)+(radius * 20)):
                cv2.circle(frame, (int(cx),int(cy)), int(radius), (150,0,150), 3)

                dist_to_center = abs((720*(4.3/radius))/(2*ouv))

                dist_center_sphere_y = abs(cy-240)*(4.3/radius)
                dist_center_sphere_x = abs(cx-340)*(4.3/radius)

                #Distance correction (using cheat function)
                dist = sqrt(dist_to_center**2 + dist_center_sphere_y**2+ dist_center_sphere_x**2)
                rayon = 0.0012*(dist**2)+ 0.1497*dist - 2.3407
                dist1 = dist - rayon

                if a == 2 or a == 1:
                    print(rayon,dist, dist1)
                    


                

                  
            
                



    
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
