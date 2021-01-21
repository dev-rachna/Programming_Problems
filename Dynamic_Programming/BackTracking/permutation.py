# -*- coding: utf-8 -*-
res=[]
arr=[1,2,3]
def permutation(used):
    if len(used)==len(arr):
        res.append(list(used))
        '''
         if duplicates are allowed the check if it in res and then add
        '''
        return
    
    for i in range(len(arr)):
        if arr[i] in used:
            continue
        
        used.append(arr[i])
        permutation(used)
        used.pop()

# permutation([])    
# print(res)
    
    
# permutation with duplicates
# mouna cs practice
import collections
res1=[]
arr1=[1,1,2]
counter=collections.Counter(arr1)
temp=[]
    
def permutation2(used):
    if len(used)==len(arr1):
        res1.append(list(used))
        return
    
    for i in counter:
        if counter[i]>0:
            used.append(i)
            counter[i]-=1
            permutation2(used)
            counter[i]+=1
            used.pop()

permutation2([])    
print(res1)