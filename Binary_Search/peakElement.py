# -*- coding: utf-8 -*-


def peakElement(arr):

    low=0
    high=len(arr)-1

    while low<=high:
        
        mid=(low+high)//2
        if mid>0 and mid<len(arr)-1:
            if arr[mid-1]<arr[mid] and arr[mid+1]<arr[mid]:
                
                return arr[mid]
            elif arr[mid-1]>arr[mid]:
                high=mid-1
            else:
                low=mid+1
        else:
            if mid==0: 
                if arr[1]<arr[0]:
                    return arr[0]
                
                else:
                    return arr[1]
            if mid==len(arr)-1:
                if arr[-1]>arr[-2]:
                    return arr[-1]
                else:
                    return -1
                    


print(peakElement([35,40,20]))
