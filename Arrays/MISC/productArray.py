# -*- coding: utf-8 -*-

'''
leetcode 238. Product of Array Except Self
Given an array nums of n integers where n > 1, 
 return an array output such that output[i] 
 is equal to the product of all the elements of nums except nums[i].

[1,2,3,4]
'''

def productExceptSelf(arr):
    left=[arr[0]]
    # right=[1]
    
    for i in range(1,len(arr)):
        left.append(left[-1]*arr[i])
    print(left)
    
    product=1
    for i in range(len(arr)-1,-1,-1):
        left[i]=left[i-1]*product
        print(i,left)
        product*=arr[i]
    
    left[0]=product
    print(left)    
productExceptSelf([1,2,3,4])    