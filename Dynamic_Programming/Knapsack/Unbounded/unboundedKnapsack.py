# -*- coding: utf-8 -*-


def uKnapsack(wt,val,W):    
    dp=[[0 for i in range(W+1)] for _ in range(len(wt)+1)]
    # print(dp)
    
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if wt[i-1]<=j:
                dp[i][j]=max(val[i-1]+dp[i][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    print(dp[-1][-1])
W = 100
val = [10, 30, 20] 
wt = [5, 10, 15]
uKnapsack(wt,val,W)
                
    

#Rod cutting problem is based on this