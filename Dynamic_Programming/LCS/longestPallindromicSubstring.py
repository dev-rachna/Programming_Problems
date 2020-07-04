# -*- coding: utf-8 -*-

'''
Given a string s, find the longest palindromic substring in s.
leetcode 5. Longest Palindromic Substring
'''

def longestPalindrome(s):
    dp=[[False for i in range(len(s))] for _ in range(len(s))]
    
    start=0
    maxi=0
    
    
    for i in range(len(s)):
        dp[i][i]=True
        
        if i<len(s)-1 and s[i]==s[i+1]:
            dp[i][i+1]=True
            start=i
            maxi=2
    
    #considering pallindromes of length 3
    k=3
    while k<=len(s):
        i=0
        while i<(len(s)-k+1):
            #index of last char
            j=i+k-1
            
            if dp[i+1][j-1] and s[i]==s[j]:
                dp[i][j]=True
                
                if k>maxi:
                    maxi=k
                    start=i
            i+=1
        k+=1
    print(s[start:start+maxi])     
    # print(dp)
    
longestPalindrome("bbbb")