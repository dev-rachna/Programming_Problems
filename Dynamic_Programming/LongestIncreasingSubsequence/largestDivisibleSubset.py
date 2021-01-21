'''
368. Largest Divisible Subset
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies:
Si % Sj = 0 or Sj % Si = 0.
If there are multiple solutions, return any subset is fine.
'''

def largestDivisibleSubset(nums):
    dp=[1 for i in range(len(nums))]
    nums.sort()
    maxi=0
    for i in range(1,len(nums)):
        for j in range(0,i):
            if nums[i]%nums[j]==0 and dp[j]+1>dp[i]:
                dp[i]=1+dp[j]
                maxi=max(maxi,dp[i])
    # print(maxi)
    prev=-1
    res=[]
    i=len(nums)-1
    while i>=0:
        if dp[i]==maxi and prev%nums[i]==0 or prev==-1:
            maxi-=1
            prev=nums[i]
            res.append(nums[i])
        i-=1

    print(res)

largestDivisibleSubset([1,2,3])




        