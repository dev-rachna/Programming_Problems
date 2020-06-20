# -*- coding: utf-8 -*-
# Author:Rachna Devasthali

def floor(arr,key):
    low=0
    high=len(arr)-1
    res=-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            print(arr[mid])
            return arr[mid]
        elif arr[mid]>key:
            high=mid-1
        else:
            res=mid
            low=mid+1
    if res==-1:
        print('no floor')
    else:
        print(arr[res])

def ceil(arr,key):
    low=0
    high=len(arr)-1
    res=-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            print(arr[mid])
            return arr[mid]
        elif arr[mid]>key:
            res=mid
            high=mid-1
        else:            
            low=mid+1
    if res==-1:
        print('no ceil')
    else:
        print(arr[res])


floor([1,2,4,5,6,12,15,17],0)
ceil([1,2,4,5,6,12,15,17],18)

        
    
    