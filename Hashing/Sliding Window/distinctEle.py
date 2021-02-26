'''
Count distinct elements in every window of size k
Difficulty Level : Medium
 Last Updated : 27 Jun, 2020
Given an array of size n and an integer k, return the count of distinct numbers in all windows of size k.
Example:

Input: arr[] = {1, 2, 1, 3, 4, 2, 3};
       k = 4
Output: 3 4 4 3

Explanation:
First window is {1, 2, 1, 3}, count of distinct numbers is 3
Second window is {2, 1, 3, 4} count of distinct numbers is 4
Third window is {1, 3, 4, 2} count of distinct numbers is 4
Fourth window is {3, 4, 2, 3} count of distinct numbers is 3

Input: arr[] = {1, 2, 4, 4};
       k = 2
Output: 2 2 1

Explanation:
First window is {1, 2}, count of distinct numbers is 2
First window is {2, 4}, count of distinct numbers is 2
First window is {4, 4}, count of distinct numbers is 1
'''
import collections
def fun(arr,k):
    left=0
    mp=collections.defaultdict(int)
    for right in range(len(arr)):
        mp[arr[right]]+=1

        if right-left+1==k:
            print(len(mp))
            mp[arr[left]]-=1
            if mp[arr[left]]<=0:
                mp.pop(arr[left])
            left+=1
    
        
fun([1, 2, 1, 3, 4, 2, 3],4)