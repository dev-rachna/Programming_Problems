# -*- coding: utf-8 -*-


def dfs(i,j,matrix):
    if i>=len(matrix) or i<0 or j>=len(matrix[0]) or j<0 or matrix[i][j]!="1":
        return
    matrix[i][j]="0"
    dfs(i+1,j,matrix)
    dfs(i-1,j,matrix)
    dfs(i,j+1,matrix)
    dfs(i,j-1,matrix)


def noOfIsland(matrix):
    
    count=0
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=="1":
                count+=1
                dfs(i,j,matrix)
    print(count)
noOfIsland([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])