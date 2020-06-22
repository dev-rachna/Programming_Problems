# -*- coding: utf-8 -*-


def bfs(li,grid):
    time=0
    while li:
        i,j,time=li.pop(0)
        
        for x,y in [[1,0],[-1,0],[0,-1],[0,1]]:
            i1=x+i
            j1=y+j
            
            if 0<=i1<len(grid) and 0<=j1<len(grid[0]) and grid[i1][j1]==1:
                grid[i1][j1]=2
                li.append([i1,j1,time+1])
                # print(grid)
    for i in grid:
        if 1 in i:
            print('-1')
            return
    
    print(time)

def rottingOranges(grid):
    li=[]
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]==2:
                li.append([i,j,0])
    
    bfs(li,grid)

rottingOranges([[2,1,1],[0,1,1],[1,0,1]])