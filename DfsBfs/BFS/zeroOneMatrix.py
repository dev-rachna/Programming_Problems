
# -*- coding: utf-8 -*-

import collections

def bfs(grid,que,visited):
    
    while que:
        i,j,d=que.popleft()
        for x,y in [[1,0],[-1,0],[0,-1],[0,1]]:
            i1=x+i
            j1=y+j
            
            if 0<=i1<len(grid) and 0<=j1<len(grid[0]) and visited[i1][j1]==0:
                visited[i1][j1]=1
                grid[i1][j1]=d+1
                que.append([i1,j1,d+1])
        
    print(grid)
    
def matrix(grid):
    que=collections.deque()
    visited=[[0  for i in range(len(grid[0]))] for _ in range(len(grid))]
    for i in range(len(grid)):       
        for j in range(len(grid[0])):
            if grid[i][j]==0:
                que.append([i,j,0])
                visited[i][j]=1
    bfs(grid,que,visited)


matrix([[0,0,0], [0,1,0],[1,1,1]])