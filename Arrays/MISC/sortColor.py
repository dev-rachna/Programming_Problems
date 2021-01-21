# -*- coding: utf-8 -*-
def fun(arr):
    left=0
    right=len(arr)-1

    index=0
    while index<right:
        if arr[index]==0:
            arr[index],arr[left]=arr[left],arr[index]
            left+=1
            index+=1
        elif arr[index]==2:
            arr[index],arr[right]=arr[right],arr[index]
            right-=1
        else:
            index+=1
    

