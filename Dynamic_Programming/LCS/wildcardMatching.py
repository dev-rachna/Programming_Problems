# -*- coding: utf-8 -*-

'''
Leetcode 44 wildcard matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

'''

def isMatch(s, p):
    dp=[[False for i in range(len(p)+1)] for _ in range(len(s)+1)]
    
    dp[0][0]=True
    
    
    for i in range(1,len(s)+1):
        dp[i][0]=False
    
    for i in range(1,len(p)+1):
        '''
        if len(s)=0 the all in p better be * to match it
        '''
        if p[i-1]=='*':
            dp[0][i]=dp[0][i-1]
    
    for i in range(1,len(s)+1):
        for j in range(1,len(p)+1):
            if s[i-1]==p[j-1] or p[j-1]=='?':
                #move ahead as that char matches
                dp[i][j]=dp[i-1][j-1]
            
            elif p[j-1]=='*':
                # you can either choose or ignore
                dp[i][j]=dp[i-1][j] or dp[i][j-1]
    
    print(dp[-1][-1])


isMatch('cbb','?b')