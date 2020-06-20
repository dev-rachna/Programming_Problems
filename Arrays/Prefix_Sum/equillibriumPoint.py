# -*- coding: utf-8 -*-


def equillibrium(arr):
    total=sum(arr)   
    curr_sum=0   
    for i in range(len(arr)):
        total-=arr[i]
        if curr_sum==total:
            print(arr[i])
            return          
        curr_sum+=arr[i]
    return -1


equillibrium([2,2,0,5,4])
        