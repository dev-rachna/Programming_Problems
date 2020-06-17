# -*- coding: utf-8 -*-


#0 0 0 0  ->(Capacity)
#0        
#0            INITIALIZATION
#| (weight)
#V
#   dp[i][j]==> dp[i elements][j weight]



val = [60, 100, 120,80] 
wt = [1, 2, 3,5]
W=8
def Knapsack():
    dp=[[0 for i in range(W+1)] for _ in range(len(wt)+1)]
    # print(dp)
    
    for i in range(1,len(wt)+1):
        for j in range(1,W+1):
            #dp starts with 0, array starts with 1 hence i-1.
            if wt[i-1]<j:
                #choose wt[i-1]=val[i-1]+dp[i-1][j-wt[i-1]] 
                # now problem reduces finding elemnt to fill capacity j-wt[i-1] (since we are considering wt[i-1])
                # Dont choose wt[i-1]=dp[i-1][j] weight j stays the same. since we dont consider wt[i-1]
                #our options reduce to i-1 elements
                dp[i][j]=max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
                
    print(dp[-1][-1])
Knapsack()


'''
at each step we have the option to either include the element or to discard it
1. If we choose i then our new capacity becomes W-wt[i]  and we have i-1 elemnts left to complete the new capacity
   hence dp becomes dp[i-1][W-wt[i]]
2. If we dont choose then also we have i-1 options to satisfy weight W


'''