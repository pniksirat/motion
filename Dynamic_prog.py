# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------
import numpy as np
grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

grid = [[0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0]]

goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    shortest_path= [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    closed = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    open=[]

    x=goal[0]
    y=goal[1]
    path=0
    open.append([path,x,y])
    closed[x][y]=1
    shortest_path[x][y]=path
    complete=0
    
    while [x,y]!=[0,0] and complete!=1 and len(open)!=0:
        open.sort()
        next=open.pop(0)
        p=next[0]
        x=next[1]
        y=next[2]
        path=p+cost
        if [x,y]==[0,0]:
            complete=1
            #shortest_path[x][y]=path
            break
        for i in range(len(delta)):
            x2=x+delta[i][0]
            y2=y+delta[i][1]
            if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                    shortest_path[x2][y2]=path
                    closed[x][y]=1
                    open.append([path,x2,y2])
                elif grid[x2][y2]==1:
                    shortest_path[x2][y2]=99

    '''
    value=[]
    for i in range(len(shortest_path)):
        value.append([99 if x==0 else x for x in shortest_path[i]])
    '''       
    value=shortest_path
    return value 


path=compute_value(grid,goal,cost)
for i in range(len(path)):
    print (path[i])