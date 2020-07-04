# -*- coding: utf-8 -*-

res=[]
arr=[10,1,2,7,6,1,5]
target=8
arr.sort()
def comboSum(rem_sum,used,start):
    if rem_sum<0:
        return
    if rem_sum==0:
        res.append(list(used))
        return
    
    for i in range(start,len(arr)):
        if i>start and arr[i]==arr[i-1]:
            continue
        
        used.append(arr[i])
        comboSum(rem_sum-arr[i],used,i+1)
        used.pop()
        
comboSum(target,[],0)
print(res)       

#repetition allowed
res=[]
arr=[2,3,6,7]
target=7
def comboSum2(rem_sum,used,start):
    if rem_sum<0:
        return
    if rem_sum==0:
        res.append(list(used))
        return
    
    for i in range(start,len(arr)):
        
        
        used.append(arr[i])
        comboSum(rem_sum-arr[i],used,i)
        used.pop()

comboSum2(target,[],0)
print(res) 