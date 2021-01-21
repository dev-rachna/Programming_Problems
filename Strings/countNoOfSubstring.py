# -*- coding: utf-8 -*-
# Given a string of lowercase alphabets, count all possible substrings 
# (not necessarily distinct) that has exactly k distinct characters.

import collections

def countkDist(str1, k): 
    res=0
    strings=[]
    n=len(str1)
    # j=0
    for i in range(n):
        count=collections.defaultdict(int)
        dist=0
        for j in range(i,n):
            if str1[j] not in count:
                dist+=1
            count[str1[j]]+=1
            # print(count)
            if dist==k:
                # print(i,j)
                res+=1
                strings.append(str1[i:j+1])
            if dist>k:
                break
         
    # print(strings)
    return res   
print(countkDist("aba",2))
