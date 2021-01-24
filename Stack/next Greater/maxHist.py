'''
84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
 find the area of largest rectangle in the histogram.
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit. 

Example:

Input: [2,1,5,6,2,3]
Output: 10
'''

def fun(arr):
    stack=[]
    maxArea=0
    arr.append(0)
    for i in range(len(arr)):
        while stack and arr[stack[-1]]>arr[i]:
            top=stack.pop()
            if len(stack)==0:
                maxArea=max(maxArea,arr[top]*i)
            else:
                maxArea=max(maxArea, arr[top]*(i-stack[-1]-1))
        stack.append(i)        
    print(maxArea)
fun([2,1,5,6,2,3])