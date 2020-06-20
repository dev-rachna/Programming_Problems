# -*- coding: utf-8 -*-
# Author:Rachna Devasthali


def firstOccurance(arr,key):
    low=0
    high=len(arr)-1
    res=-1
    while low<=high:
        mid=(low+high)//2
        #mid=low + (high-low)//2 to avoid integer overflow
        if arr[mid]==key:
            res=mid
            high=mid-1
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    print(res)
    return res
    
def lastOccurance(arr,key):
    low=0
    high=len(arr)-1
    res=-1
    while low<=high:
        mid=(low+high)//2       
        if arr[mid]==key:
            res=mid
            low=mid+1
        elif arr[mid]>key:
            high=mid-1
        else:
            low=mid+1
    print(res)
    return res

#count number of elemnts in a sorted array
first=firstOccurance([1,1,3,4,5,5,5,5,6,6],6)          
second=lastOccurance([1,1,3,4,5,5,5,5,6,6],6)

print('No of elements',second-first+1)