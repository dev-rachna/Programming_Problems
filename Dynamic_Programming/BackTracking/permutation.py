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
    
    
#permutation with duplicates
# res1=[]
# arr1=[1,1,2]
# temp=[]
# for i in range(len(arr)):
#     temp.append(False)
    
# def permutation2(used,temp):
#     if len(used)==len(arr):
#         res1.append(list(used))
#         return
    
#     for i in range(len(arr1)):
#         if temp[i] or (i>0 and arr1[i]==arr1[i-1] and not(temp[i-1])):
            
#             continue
#         temp[i]=True
#         used.append(arr1[i])
#         permutation(used)
#         temp[i]=False
#         used.pop()

# permutation2([],temp)    
# print(res1)