from collections import deque
import time
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", "#", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

parent={}
checker=deque()
visted=set()
start_pos={}
start=None
def find_start():
    for i in maze:
        for j in i:
            if j=="O":
                checker.append((maze.index(i),i.index(j)))
                start=(maze.index(i),i.index(j))

                break
find_start()
def find_nigh(maze_cord,list_cord):
    global maze

    try:
        #down
        if maze[maze_cord+1][list_cord]==" " or maze[maze_cord+1][list_cord]=="X":
            if (maze_cord+1,list_cord) not in visted:
                checker.append((maze_cord+1,list_cord))
                visted.add((maze_cord+1,list_cord))
                print("down")
                parent[(maze_cord+1,list_cord)]=(maze_cord,list_cord)
    except IndexError:
        pass
        
    try:
        #up
        if maze[maze_cord-1][list_cord]==" " or maze[maze_cord-1][list_cord]=="X":
            if (maze_cord-1,list_cord) not in visted:
                checker.append((maze_cord-1,list_cord))
                visted.add((maze_cord-1,list_cord))
                print("up")
                parent[(maze_cord-1,list_cord)]=(maze_cord,list_cord)
    except IndexError:
        pass
    try:
        #right
        if maze[maze_cord][list_cord+1]==" " or maze[maze_cord][list_cord+1]=="X":
            if (maze_cord,list_cord+1) not in visted:
                checker.append((maze_cord,list_cord+1))
                visted.add((maze_cord,list_cord+1))
                parent[(maze_cord,list_cord+1)]=(maze_cord,list_cord)
                print("right")
    except IndexError:
        pass
    try:
        #left
        if maze[maze_cord][list_cord-1]==" " or maze[maze_cord][list_cord-1]=="X":
            if (maze_cord,list_cord-1) not in visted:
                checker.append((maze_cord,list_cord-1))
                visted.add((maze_cord,list_cord-1))
                parent[(maze_cord,list_cord-1)]=(maze_cord,list_cord)
                print("left")
    except IndexError:
        pass

def check_if_end(maze_cord,list_cord):
    global continued
    if maze[maze_cord][list_cord]=="X":
        continued=False
cur=None
while True:
    try:
        list1=checker.popleft()
    except IndexError:
        print("finished")
    visted.add(list1)
    maze_cord=list1[0]
    list_cord=list1[1]
    continued=True
    check_if_end(maze_cord,list_cord)
    cur=list1
   
    print(continued)
    if continued:
        find_nigh(maze_cord,list_cord)
        
    else:
        print("found")
        print(parent)
        break
ads=None
while True:
    if cur!=start:
        ads=parent[cur]
        print("way",ads)
    else:
        break
    cur=ads
    
    




    

        
    
    
         

