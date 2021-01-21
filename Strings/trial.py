
import collections
def numberOfSubarrays(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        count=0
        left=0
        res=0
        que=collections.deque([])
        que.append(-1)
        for right in range(len(nums)):
            
            if nums[right]%2==1:
                que.append(right)
            print(right,que)
            if len(que)>k+1:
                que.popleft()
            if len(que)==k+1:
                print(que)
                res+=que[1]-que[0]
            
            print('r',res)
            
        
        return res


numberOfSubarrays([0,0,1,0,1],2)