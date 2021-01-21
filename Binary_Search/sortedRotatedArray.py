# -*- coding: utf-8 -*-
# Author:Rachna Devasthali

def findPivot(arr):   
    low=0
    high=len(arr)-1

    if arr[low]<=arr[high]:
        print(arr[low])
        return 
    
    while low<=high:
        mid=(low+high)//2        
        if arr[mid]>arr[mid+1]:
            print(arr[mid])
            return
        elif arr[low]>arr[mid]:
            high=mid-1
        else:
            low=mid+1


def searchSortedRotatedarray(arr,key):
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2 
        # print(mid,high,low)
        if arr[mid]==key:
            print('found')
            return
        elif arr[low]<=arr[mid]:
            if arr[low]<=key<arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if arr[mid]<=key<=arr[high]:
                low=mid+1
                
            else:
                high=mid-1
    print('not found')
        
    
findPivot([40,100,1,2,3,4])    
searchSortedRotatedarray([40,100,1,2,3,4],40)          
    
