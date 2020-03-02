import cv2
import numpy as np
import math
img = np.zeros((500,700,3), np.uint8)

x=0.001
y=0.001
m=0
p=0
xx=0
yy=0

while True:
    tickmark=cv2.getTickCount()
    key = cv2.waitKey(1)
    if key == 27:
        break
    cv2.line(img, (int(x),int(y)), (int(xx)+200, int(yy)+200), (0,0,0), 1)
    cv2.line(img, (int(x),int(y)), (-int(xx)+200, -int(yy)+200), (0,0,0), 1)
    #if key != -1:
    #   print(key)
    if key == 122:
        cv2.circle(img, (int(x),int(y)), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        y-=3
        
    if key== 115:
        cv2.circle(img, (int(x),int(y)), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        y+=3
        
    if key == 113:
        cv2.circle(img, (int(x),int(y)), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        x-=3

    if key == 100:
        cv2.circle(img, (int(x),int(y)), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        x+=3

    if key == 97:
        print(fps)
    cv2.circle(img, (int(x),int(y)), 1, (0,0,255), 2)
    cv2.circle(img, (200,200), 16, (150,0,150), 2)

    cv2.line(img, (200,200), (int(xx)+200,int(yy)+200), (0,0,0), 1)
    cv2.line(img, (200,200), (200-int(xx),200-int(yy)), (0,0,0), 1)

    

    a = (200-y)/(200-x)
    m = -1/a
    p = y-m*x
    
    xx = 16*math.cos(math.atan(m))
    yy = 16*math.sin(math.atan(m))
    
    cv2.line(img, (int(x),int(y)), (int(xx)+200, int(yy)+200), (0,200,0), 1)
    cv2.line(img, (int(x),int(y)), (-int(xx)+200, -int(yy)+200), (0,200,0), 1)
    
    cv2.line(img, (200,200), (int(xx)+200,int(yy)+200), (0,100,100), 1)
    cv2.line(img, (200,200), (200-int(xx),200-int(yy)), (0,100,100), 1)
    cv2.line(img, (200,200), (int(x),int(y)), (255,0,0), 1)
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(img, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow("simu",img)
    cv2.putText(img, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
    
cv2.destroyAllWindows()
