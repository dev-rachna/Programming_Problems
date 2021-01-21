'''
55. Jump Game
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5
'''

def canJump(nums):
    reachable=0

    for i in range(len(nums)):
        if reachable<i:
            return False
        
        reachable=max(reachable,i+nums[i])  

    return True


'''
45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''
#approach 1 using DP
def jump(nums):
    dp=[float('inf') for i in range(len(nums))]
    dp[0]=0

    for i in range(1,len(nums)):
        for j in range(i):
            if j+nums[j]>=i:
                dp[i]=min(dp[i],dp[j]+1)
    
#Greedy Approach
def jump2(nums):
    if len(nums)<=1:
            return 0
    jump=1
    farthest=nums[0]
    current_end=nums[0]
    
    for i in range(1,len(nums)):
        if i==len(nums)-1:
            return jump
        farthest=max(farthest,i+nums[i])
        if i==current_end:
            jump+=1
            current_end=farthest
    
    return jump




