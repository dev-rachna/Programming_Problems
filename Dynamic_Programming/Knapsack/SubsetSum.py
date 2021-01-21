# -*- coding: utf-8 -*-

arr=[1,2,3,4,5,9]
s=8


'''
<-----sum----->
^
|
array elements
|
v

'''
#Check if there exits a subset that has given sum
def subsetSum(arr,s):
    dp=[[False for i in range(s+1)] for _ in range(len(arr)+1)]
    
    #initialize col 0 with 1
    #if target sum is 0 the we can always have null set that satisfies the condition
    for i in range(0,len(arr)+1):
        dp[i][0]=True
    
    for i in range(1,len(arr)+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    
    print(dp[-1][-1])
    

#Count no. of subsets with given sum
def countSubsetSum(arr,s):
    dp=[[0 for i in range(s+1)] for _ in range(len(arr)+1)]
    
    for i in range(0,len(arr)+1):
        dp[i][0]=1
        
    for i in range(1,len(arr)+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                
                dp[i][j]=dp[i-1][j-arr[i-1]]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    
    print(dp[-1][-1])
    return dp[-1][-1]
    
# 416. Partition Equal Subset Sum leetcode
def canPartition(arr,s):
    if s%2==0:
        
        s=s//2
        return subsetSum(arr,s)
        
    
subsetSum(arr,s)
countSubsetSum(arr,s)
canPartition(arr,s)
    