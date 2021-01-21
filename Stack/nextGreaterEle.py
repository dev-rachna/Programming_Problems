'''
Next greater element to right

ex:
i/p: [5,4,9,13]
o/p: [9,9,13,-1]
'''
def nextGreaterElement(arr):
    stack=[]
    result=[]
    i=len(arr)-1
    for i in range(len(arr)-1,-1,-1):
        
        while stack and arr[i]>stack[-1]:
            stack.pop()
        
        if len(stack)==0:
            result.append(-1)
        else:
            result.append(stack[-1])
        stack.append(arr[i])

    result.reverse()
    print(result)


nextGreaterElement([1,2,3,4])


'''
Next greater element to left

ex:
i/p: [5,4,9,13]
o/p: [-1,5,-1,-1]
'''
def nextGreaterElementLeft(arr):
    stack=[]
    result=[]

    for i in range(len(arr)):
        
        while stack and arr[i]>stack[-1]:
            stack.pop()
        
        if not(stack):
            result.append(-1)
        else:
            result.append(stack[-1])
    
        stack.append(arr[i])

    print(result)

nextGreaterElementLeft([9,8,7,6])

