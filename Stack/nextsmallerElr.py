'''
similar to next greater to left . instead search fro next smaller to left and right

'''

def nextSmallerRight(arr):
    stack=[]
    result=[]
    i=len(arr)-1
    for i in range(len(arr)-1,-1,-1):
        if len(stack)==0:
            stack.append(-1)
            result.append(-1)
        else:
            while stack and arr[i]<stack[-1]:
                stack.pop()
            
            if len(stack)==0:
                result.append(-1)
            else:
                result.append(stack[-1])
        stack.append(arr[i])

    result.reverse()
    print(result)

nextSmallerRight([5,4,8,1,0])
    

def nextSmallerLeft(arr):
    stack=[]
    result=[]

    for i in range(len(arr)):
        if len(stack)==0:
            result.append(-1)
            stack.append(-1)
        else:
            while stack and arr[i]<stack[-1]:
                stack.pop()
            
            if not(stack):
                result.append(-1)
            else:
                result.append(stack[-1])
        
        stack.append(arr[i])

    print(result)


nextSmallerLeft([5,4,8,1,0])