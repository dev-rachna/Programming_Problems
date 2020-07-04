# -*- coding: utf-8 -*-

'''
leetcode 221. Maximal Square
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area
'''

def maximalSquare(matrix):
    
    dp=[[0 for i in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    largest=0
    
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            
            if matrix[i-1][j-1]=="1":
                dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                
            largest=max(largest,dp[i][j])
    
    return(largest)

print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))