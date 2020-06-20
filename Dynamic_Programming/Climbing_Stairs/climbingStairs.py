# -*- coding: utf-8 -*-


def climbStairs(n):
    
    dp=[0 for i in range(n+1)]
    dp[0]=1
    #if one steps then 1 way to climb it 
    dp[1]=1
    
    for i in range(2,n+1):
        # you can reach step i by taking step i-1 or step i-2
        dp[i]=dp[i-1]+dp[i-2]
    
    print(dp[n])
    
climbStairs(5)
    
            
