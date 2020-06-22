# -*- coding: utf-8 -*-


# array is sorted
def twoSum(arr,target):
    l=0
    r=len(arr)-1
    
    while l<r:
        sm=arr[l]+arr[r]
        if sm==target:
            print(arr[l],arr[r])
            return (arr[l],arr[r])
        elif sm<target:
            l+=1
        else:
            r-=1
    return -1


#array is not sorted
def twoSum2(arr,target):
    set1=set()
    for i in arr:
        if target-i in set1:
            print(i,target-i)
            return
        else:
            set1.add(i)
    return -1
    


print(twoSum2([3,4,5,7,2], 6))
        
    

