import cv2
import numpy as np
import math
img = np.zeros((700,900,3), np.uint8)

x=0.001
y=0.001
m=0
p=0
xx=0
yy=0
rayon=0
dist=0


obst= []
def mouse_drawing(event, x, y, flags, params):
    global obst
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (int(x), int(y)), 7, (255,255,255), 1)
        obst.append([x,y])
        
        

    
    
        

while True:
    print(obst)
    tickmark=cv2.getTickCount()
    key = cv2.waitKey(1)
    if key == 27:
        break
    cv2.line(img, (int(x),int(y)), (int(xx)+200, int(yy)+200), (0,0,0), 1)
    cv2.line(img, (int(x),int(y)), (-int(xx)+200, -int(yy)+200), (0,0,0), 1)
    cv2.circle(img, (int(x),int(y)), int(rayon), (0,0,0), 1)
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

    dist = math.sqrt((200-x)**2+(200-y)**2)
    dist=dist/2
    rayon = 0.0012*(dist**2)+ 0.1497*dist - 2.3407
    cv2.circle(img, (int(x),int(y)), int(rayon), (0,0,255), 1)
    
    
    
    cv2.line(img, (int(x),int(y)), (int(xx)+200, int(yy)+200), (0,200,0), 1)
    cv2.line(img, (int(x),int(y)), (-int(xx)+200, -int(yy)+200), (0,200,0), 1)
    
    cv2.line(img, (200,200), (int(xx)+200,int(yy)+200), (0,100,100), 1)
    cv2.line(img, (200,200), (200-int(xx),200-int(yy)), (0,100,100), 1)
    cv2.line(img, (200,200), (int(x),int(y)), (255,0,0), 1)

    for i in obst:
        cv2.circle(img, (int(i[0]),int(i[1])), 7, (255,255,255), 1)


    
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(img, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow("simu",img)
    cv2.putText(img, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
    
    cv2.setMouseCallback("simu", mouse_drawing)
    
cv2.destroyAllWindows()

