# -*- coding: utf-8 -*-

def dfs(image,i,j,newColor,source):
    if i>=len(image) or i<0 or j>=len(image[0]) or j<0 or image[i][j]!=source:
        return
    
    image[i][j]=newColor
    dfs(image,i+1,j,newColor,source)
    dfs(image,i-1,j,newColor,source)
    dfs(image,i,j+1,newColor,source)
    dfs(image,i,j-1,newColor,source)
    


def floodFill(image, sr, sc, newColor):   
    dfs(image,sr,sc,newColor,image[sr][sc])
    print(image)


floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)