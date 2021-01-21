'''
76. Minimum Window Substring

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

'''

import collections

def minWindow(s, t):
    T=[0]*128
    count=0
    for i in t:
        T[ord(i)]+=1
    left=0
    right=0
    minLen=float('inf')
    while right<len(s):
        T[ord(s[right])]-=1
        if T[ord(s[right])]>=0:
            
            count+=1
           
        print(right,count)
        while count==len(t) and left<right:
            print(minLen,'m',count)
            if minLen>right-left+1:
                minLen=right-left+1
                res=s[left:right+1]


            

            T[ord(s[left])]+=1
            if T[ord(s[left])]>0:
               
                count-=1
                
            left+=1
            print(left,right,count)
                 
        right+=1
    print(res)
    return res

        

minWindow('DBAECAB','ABC')