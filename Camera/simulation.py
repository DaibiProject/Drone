import cv2
import numpy as np

img = np.zeros((500,700,3), np.uint8)

x=0
y=0

while True:
    tickmark=cv2.getTickCount()
    key = cv2.waitKey(1)
    if key == 27:
        break

    #if key != -1:
    #   print(key)
    if key == 122:
        cv2.circle(img, (x,y), 1, (0,0,0), 2)
        y-=2
        
    if key== 115:
        cv2.circle(img, (x,y), 1, (0,0,0), 2)
        y+=2
        
    if key == 113:
        cv2.circle(img, (x,y), 1, (0,0,0), 2)
        x-=2
        
    if key == 100:
        cv2.circle(img, (x,y), 1, (0,0,0), 2)
        x+=2

    if key == 97:
        print(fps)
    cv2.circle(img, (x,y), 1, (0,0,255), 2)
    cv2.circle(img, (200,200), 10, (0,255,0), 2)

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    
    cv2.imshow("simu",img)
cv2.destroyAllWindows()
