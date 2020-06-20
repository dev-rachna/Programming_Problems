# -*- coding: utf-8 -*-

def lcs(s1,s2):
    
    dp=[x[:] for x in [[0]*(len(s1)+1)]*(len(s2)+1)]
    #print(dp)
    #dp[i][j] -- taking i letters from s2 and taking j letters from s1
    #dp table starts index 1 but string starts from 0 so initialize row 0 col 0 with 0
    for i in range(1,len(s2)+1):
        for j in range(1,len(s1)+1):
            if s2[i-1]==s1[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
                
            else:
                #take max( leave either current element from s1 or leave current element of s2 )
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    # print(dp)
    # print('max lcs',dp[-1][-1])
    return dp[-1][-1]       

print(lcs("geek","ek"))

def lcsPrint(A, B):
            n, m = len(A), len(B)
            dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
            for i in range(n):
                for j in range(m):
                    if A[i] == B[j]:
                        dp[i + 1][j + 1] = dp[i][j] + A[i]
                        
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
            # print(dp)
            return dp[-1][-1]        

print(lcsPrint("geek","ek"))



#leetcode problems based on this problem
#1. Uncrossed line