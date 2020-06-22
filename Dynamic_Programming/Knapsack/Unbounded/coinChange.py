# -*- coding: utf-8 -*-

def coinChangeCount(coin,amt):    
    dp=[[0 for i in range(amt+1)] for _ in range(len(coin)+1)]
    
    #always have 1 way (ie to exclude the coin)
    for i in range(len(dp)):
        dp[i][0]=1
    
    for i in range(1,len(dp)):
        for j in range(1,len(dp[0])):
            if coin[i-1]<=j:
                dp[i][j]=dp[i][j-coin[i-1]]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    print(dp[-1][-1])

#1d array dp (thecodingworld)
def coinChangeCount2(coin,amt): 
    dp=[0 for i in range(amt+1)]
    dp[0]=1
    for i in coin:
        for j in range(i,amt+1):
            if i<=j:
                dp[j]+=dp[j-i]
    print(dp[-1])
    

def minimumCoins(coins,amount):    
    dp=[[0 for i in range(amount+1)] for _ in range(len(coins)+1)]
    
    #if sum is zero you need infinite number of coins
    for i in range(amount+1):
            dp[0][i]=float('inf')
    
    #initialize row 1 
    # only if the sum is divisible by first element then add it else it takes infinite coins.
    for j in range(1,amount+1):
        if j%coins[0]==0:
            dp[1][j]=j//coins[0]
        else:
            dp[1][j]=float('inf')
      
    for i in range(1,len(coins)+1):            
        for j in range(1,amount+1):
            if coins[i-1]<=j:
                dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
            
   
    if dp[-1][-1]==float('inf'):
        return -1
    return (dp[-1][-1])
# print(minimumCoins([1,2,5],5))
coinChangeCount2([1,2,3],4)