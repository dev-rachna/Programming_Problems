# -*- coding: utf-8 -*-

'''
767. Reorganize String
Given a string S, check if the letters can be rearranged so that two characters 
that are adjacent to each other are not the same
'''
import collections
from heapq import heapify,heappush,heappop

def reorganizeString(s):
    
    heap=[]
    heapify(heap)
    
    count=collections.Counter(s)
    for i in count:
        heappush(heap,[-1*count[i],i])
    
    # print(heap)
    res=''
    while len(heap)>1:
        element1=heappop(heap)
        element2=heappop(heap)
        
        res+=element1[1]
        res+=element2[1]
        
        element1[0]+=1
        element2[0]+=1
        
        if element1[0]<0:
            heappush(heap,element1)
        if element2[0]<0:
            heappush(heap,element2)
        
    
    if len(heap)!=0:
        element=heappop(heap)
        if element[0]==-1:
            res+=element[1]
        else:
            return -1

    return res
    
    
print(reorganizeString("abbabbaaab") )
    

