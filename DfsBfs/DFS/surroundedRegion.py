# -*- coding: utf-8 -*-


def dfs(i,j,grid):
    if i>=len(grid) or i<0 or j>=len(grid[0]) or j<0 or grid[i][j]!="O":
        return
    
    grid[i][j]="*"
    #top down right left
    dfs(i+1,j,grid)
    dfs(i-1,j,grid)
    dfs(i,j+1,grid)
    dfs(i,j-1,grid)



def solve(grid):
    #corner cols
    for i in range(len(grid)):
        if grid[i][0]=='O':
            dfs(i,0,grid)
        if grid[i][-1]=='O':
            dfs(i,len(grid[0])-1,grid)
   
    #corner row        
    for j in range(len(grid[0])):
        if grid[0][j]=='O':
            dfs(0,j,grid)
        if grid[-1][j]=='O':
            dfs(len(grid)-1,j,grid)
    
    #change grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='*':
                grid[i][j]='O'
            elif grid[i][j]=='O':
                grid[i][j]='X'
    
    print(grid)

solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])