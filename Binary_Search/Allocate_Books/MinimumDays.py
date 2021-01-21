'''
leetcode 1482. Minimum Number of Days to Make m Bouquets
Given an integer array bloomDay, an integer m and an integer k.
We need to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.
'''

def isValid(bloomDay, m, k,mid):
    flower=0
    bouquet=0

    for i in bloomDay:
        if i>mid:
            flower=0
        else:
            flower+=1

        if flower>=k:
            flower=0
            bouquet+=1

    return bouquet



def minDays(bloomDay, m, k):

    if len(bloomDay)<m*k:
        return -1

    low=1
    high=max(bloomDay)
    
    while low<high:
        mid=(low+high)//2
        bq=isValid(bloomDay,m,k,mid)
        
        if bq<m:
            low=mid+1
        else:
            high=mid
    
    return low
    
    
      
print(minDays([10,10],1,1))

