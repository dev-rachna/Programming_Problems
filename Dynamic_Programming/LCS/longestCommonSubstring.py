# -*- coding: utf-8 -*-

def lcsubstring(s1,s2):
    
    dp=[x[:] for x in [[0]*(len(s1)+1)]*(len(s2)+1)]
    
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1]==s1[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=0
    
    return(dp[-1][-1])

lcsubstring("abc","a")

