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
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        y-=2
        
    if key== 115:
        cv2.circle(img, (x,y), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        y+=2
        
    if key == 113:
        cv2.circle(img, (x,y), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        x-=2
        
    if key == 100:
        cv2.circle(img, (x,y), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        x+=2

    if key == 97:
        print(fps)
    cv2.circle(img, (x,y), 1, (0,0,255), 2)
    cv2.circle(img, (200,200), 16, (0,255,0), 2)

    u = [-200 - x,200 + y]

    cv2.line(img, (200,200), (int(x),int(y)), (255,0,0), 1)
    if u[0] == 0:
        u[0] = 0.00001
    v = u[1]/u[0]
    print(200, 200 +v*10)

    cv2.line(img, (200,200), (210, (200 + int(v)*10)), (255,0,0), 1)

    
    cv2.circle(img, (10, int(v*10)), 1, (0,255,0),1)
    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(img, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow("simu",img)
    cv2.putText(img, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
    
cv2.destroyAllWindows()
