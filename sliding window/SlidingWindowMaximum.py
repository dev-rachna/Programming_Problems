'''
239. Sliding Window Maximum

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
import collections
def fun(nums,k):
    maxque=collections.deque([])
    result=[]
    count=0
    left=0
    for right in range(len(nums)):
        count+=1
        while maxque and nums[right]>maxque[-1]:
            maxque.pop()
        maxque.append(nums[right])
        if count==k:
            result.append(maxque[0])
            count-=1
            if maxque[0]==nums[left]:
                maxque.popleft()
            left+=1
    
    print(result)

fun([1,3,-1,-3,5,3,6,7],3)