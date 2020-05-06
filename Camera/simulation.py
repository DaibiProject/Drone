import cv2
import numpy as np
import math
import time
from random import randint

#Variable declaration
img = np.zeros((700,900,3), np.uint8)
b = 0
x=0.001
y=0.001
m=0
p=0
xx=0
yy=0
rayon=0
dist=0
x1=0
y1=0
obst= []
taille_case = 20
cx = 0
cy = 0
incr = 0
map_ = []

detection = [0,0,0,0,0]


#grid display
for i in range(int(700/taille_case)):
    map_.append([0])
    for y in range(int((900/taille_case))-1):
        map_[i].append(0)


#Obstacle class
class Obstacle:
    global map_
    global taille_case
    obst = []
    index = 0
    
    def __init__(self):
        self.x=0
        self.y=0
        self.index = Obstacle.index
        Obstacle.index += 1
        Obstacle.obst.append([x,y])
        
    def set_value(self, xx,yy):
        self.x = xx
        self.y = yy
        self.x1 = xx/taille_case
        self.y1 = yy/taille_case
        Obstacle.obst[self.index]=[self.x,self.y]
        map_[int(self.y1)][int(self.x1)] = 3

    def get_valuex(self):
        return self.x

    def get_valuey(self):
        return self.y


#class Node - Pathfinding' part
class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

#Path maker (A* version)
def astar(map_, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    open_list = []
    closed_list = []

    open_list.append(start_node)
    
    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
                
        open_list.pop(current_index)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path
        
        children = []

        rand = randint(1,4)
        if rand == 1:
            adj = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        elif rand == 2:
            adj = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        elif rand == 3:
            adj = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        elif rand == 4:
            adj = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for new_position in adj:
            
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            if node_position[0] > (len(map_) - 1) or node_position[0] < 0 or node_position[1] > (len(map_[len(map_)-1]) -1) or node_position[1] < 0:
                continue

            if map_[node_position[0]][node_position[1]] == 1:
                continue

            new_node = Node(current_node, node_position)
            fill_case(node_position[1]*taille_case,node_position[0]*taille_case,-700,-700,(60,60,60))
             
            children.append(new_node)

        for child in children:

            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0])**2) + ((child.position[1] - end_node.position[1])**2)
            child.f = child.g + child.h
            
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            open_list.append(child)    


#Mouse obstacle
def mouse_drawing(event, x, y, flags, params):
    global obst
    global incr
    
    if event == cv2.EVENT_LBUTTONDOWN:
        if b==1 or b==2:
            cv2.circle(img, (int(x), int(y)), 7, (255,255,255), 1)
        obst.append(Obstacle())
        obst[-1].set_value(x,y)


#Generic function - very usefull 
def fill_case(x,y,cx,cy,color):
   
    cv2.rectangle(img, (cx,cy),(cx+taille_case,cy+taille_case),(0,0,0),-1)
    cx = int(x/taille_case)*taille_case
    cy = int(y/taille_case)*taille_case
    cv2.rectangle(img, (cx,cy),(cx+taille_case,cy+taille_case),color,-1)


#Main loop
while True:
    tickmark=cv2.getTickCount()
    key = cv2.waitKey(1)
    if key == 27:
        break

    i = 0
    while i <900:
        cv2.line(img, (int(i), 0), (int(i), 700), (30,30,30))
        i+= taille_case
    i = 0
    while i < 700:
        cv2.line(img, (0, int(i)), (900, int(i)), (30,30,30))
        i+= taille_case
        
    cv2.line(img, (int(x),int(y)), (int(xx)+200, int(yy)+200), (0,0,0), 1)
    cv2.line(img, (int(x),int(y)), (-int(xx)+200, -int(yy)+200), (0,0,0), 1)
    cv2.circle(img, (int(x),int(y)), int(rayon), (0,0,0), 1)
        
    for i in obst:
        if b==1 or b==2:
            cv2.line(img, (int(x),int(y)),((i.get_valuex()),int(i.get_valuey())), (0,0,0))

        if map_[int(i.get_valuey()/taille_case)][int(i.get_valuex()/taille_case)] == 3:
            fill_case(i.get_valuex(),i.get_valuey(), -100, -100,(20,20,20))

        elif map_[int(i.get_valuey()/taille_case)][int(i.get_valuex()/taille_case)] == 1:
            fill_case(i.get_valuex(),i.get_valuey(), -100, -100,(50,20,20))
    fill_case(x,y,cx,cy,(0,0,0))

    #Key mapping
    if key == 122:
        cv2.circle(img, (int(x),int(y)), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        y-=5
        
    if key== 115:
        cv2.circle(img, (int(x),int(y)), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        y+=5
        
    if key == 113:
        cv2.circle(img, (int(x),int(y)), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        x-=5

    if key == 100:
        cv2.circle(img, (int(x),int(y)), 1, (0,0,0), 2)
        cv2.line(img, (200,200), (int(x),int(y)), (0,0,0), 1)
        x+=5

    fill_case(x,y,cx,cy,(20,20,40))

    if key == 97:
        
        if b == 1:
            b = 2
        
        elif b == 0:
            b = 1

        elif b == 2:
            b = 0
            
    if key == 9:
        start = (int(y/taille_case),int(x/taille_case))
        end = (10,10)
        path = astar(map_,start,end)
        print(path)
        print(Obstacle.obst)
        for i in path:
            fill_case(i[1]*taille_case,i[0]*taille_case,-700,-700,(100,100,100))
            map_[i[0]][i[1]]=2
        print(map_)
        print(detection)

    if b == 2:
        print(fps)
        print(obst)
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



    #Simulate proximity alert
    x1 = int(x/taille_case)
    y1 = int(y/taille_case)

    for i in range(1,4):
        if map_ != []:
            h = 4-i
            if map_[y1][x1 + h] == 1 or map_[y1][x1 + h] == 3:
                detection[1] = h
                if map_[y1][x1 + h] == 3:
                    map_[y1][x1 + h] == 1
                
                
            if map_[y1][x1 - h] == 1 or map_[y1][x1 - h] == 3:
                detection[3] = h
                if map_[y1][x1 - h] == 3:
                    map_[y1][x1 - h] == 1
                    
            
            if map_[y1 + h][x1] == 1 or map_[y1 + h][x1] == 3:
                detection[2] = h
                if map_[y1 + h][x1] == 3:
                    map_[y1 + h][x1] == 1
                
            if map_[y1 - h][x1] == 1 or map_[y1 - h][x1] == 3:
                detection[0] = h
                if map_[y1 - h][x1] == 3:
                    map_[y1 - h][x1] == 1
                


    
    if b == 1 or b == 2:
        for i in obst:
            cv2.circle(img, (int(i.get_valuex()),int(i.get_valuey())), 7, (255,255,255), 1)
            cv2.line(img, (int(x),int(y)),(int(i.get_valuex()),int(i.get_valuey())), (100,100,100))

    fps=cv2.getTickFrequency()/(cv2.getTickCount()-tickmark)
    cv2.putText(img, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)
    cv2.imshow("simu",img)
    cv2.putText(img, "FPS: {:05.2f}".format(fps), (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)
    
    cv2.setMouseCallback("simu", mouse_drawing)
    
cv2.destroyAllWindows()

