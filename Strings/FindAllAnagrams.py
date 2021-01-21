# -*- coding: utf-8 -*-

'''
leetcode 438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
'''
import collections
def findAnagrams(s, p):
    phash=collections.Counter(p)
    shash=collections.defaultdict(int)
    
    for i in range(len(p)):
        shash[p[i]]+=1
    res=[]
    i=0
    j=len(p)-1
    while j<len(s)-1:
        if phash==shash:
            res.append(i)
        shash[s[i]]-=1   
        if shash[s[i]]<=0:
            shash.pop(s[i])
        i+=1
        j+=1
        shash[s[j]]+=1
            
    if phash==shash:
            res.append(i) 
    print(res)
'''  
consise code:
    
    res = []
        pCounter = Counter(p)
        sCounter = Counter(s[:len(p)-1])
        for i in range(len(p)-1,len(s)):
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res
'''
findAnagrams('bacb','abc')  