# -*- coding: utf-8 -*-


res=[]
nums=[1,2,3]
#subset without duplicates
def subset(arr,start):
    res.append(list(arr))
    
    for i in range(start,len(nums)):
        arr.append(nums[i])
        subset(arr,i+1)
        arr.pop()
    
subset([],0)
print(res)

