# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space


grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']



def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right
    opened=[]
    closed=[]
    opened=[[init,0]]
    g_value=[0]
    active=True
    g=0
    while (len(opened)!=0 and opened[0][0]!=goal):
        
        opened.sort(key=lambda x: x[1])
        if opened[0]==goal:
            active=False
        else:
            # go through the neighbours and if they are not traced then walk through them
             
            for i in range(4):
                m=delta[i][0]+opened[0][0][0] #row
                n=delta[i][1]+opened[0][0][1]  #colmn
                g=opened[0][1]
                #res1 = any([[m,n],g] in sublist for sublist in opened) 
                #res2 = any([[m,n],g] in sublist for sublist in closed)
                res1=[m,n] in (x[0] for x in opened)
                res2=[m,n] in (x[0] for x in closed)
                if ((len(grid)>m>=0) and (len(grid[0])>n>=0) and res1==False and res2==False): # if inside the grid and was not opened previously
                    if grid[m][n]==0:
                        g+=1
                        opened.append([[m,n],g])
            closed.append(opened.pop(0))          
                
                    
    last=opened[0] 
    path=[last[1],last[0][0],last[0][1]]           
    return path

search(grid,init,goal,cost)