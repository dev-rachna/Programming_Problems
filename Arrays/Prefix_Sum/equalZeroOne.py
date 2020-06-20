# -*- coding: utf-8 -*-

# leetcode  Contiguous Array
def equalZeroOne(arr):
    counter={}
    maxi=0
    count=0
    for i,j in enumerate(arr):
        if j==0:
            count-=1
        else:
            count+=1
            
        if count in counter:            
            maxi=max(maxi,i-counter[count])           
        else:
            counter[count]=j
      
    print(maxi)

equalZeroOne([0,0,1,1,1,0])      
    