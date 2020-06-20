# -*- coding: utf-8 -*-

import SubsetSum

def targetSum(arr,target):
    sumCal=(sum(arr)+target)//2
    SubsetSum.countSubsetSum(arr,sumCal)
    

targetSum([1,2,3,4,5,9],8)    

