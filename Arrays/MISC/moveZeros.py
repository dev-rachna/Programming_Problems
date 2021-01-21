# -*- coding: utf-8 -*-

def fun(arr):
    left=0
    for i in range(len(arr)):
        if arr[i]!=0:
            arr[i],arr[left]=arr[left],arr[i]
            left+=1
        
    print(arr)    

fun([0,2,4,0,5]) 