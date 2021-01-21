'''
Given an array of integers, count number of subarrays (of size more than one) that are strictly increasing.
Expected Time Complexity : O(n)
Expected Extra Space: O(1)

Input: arr[] = {1, 4, 3}
Output: 1
There is only one subarray {1, 4}

Input: arr[] = {1, 2, 3, 4}
Output: 6
There are 6 subarrays {1, 2}, {1, 2, 3}, {1, 2, 3, 4}
                      {2, 3}, {2, 3, 4} and {3, 4}

Input: arr[] = {1, 2, 2, 4}
Output: 2
There are 2 subarrays {1, 2} and {2, 4}

'''
def countIncreasing(arr, n): 
    length=1
    count=0
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            length+=1
        else:
            count+=(length*(length-1))//2
            length=1
    
    if length!=1:
        count+=(length*(length-1))//2
    
    return count

arr = [1, 2, 3, 4] 
n = len(arr) 
  
print ("Count of strictly increasing subarrays is", 
                        (countIncreasing(arr, n))) 



