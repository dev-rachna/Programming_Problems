#IB sorting1
# /|\    .....        \|/
#  pivot               pivot from end


def fun(arr):
    start,end=-1,-1

    #start
    for i in range(1,len(arr)):
        if arr[i-1]>arr[i]:
            start=i-1
            break
    
    #end
    for i in range(len(arr)-1,0,-1):
        if arr[i]<arr[i-1]:
            end=i
            break
    
    #confirm
    minVal=min(arr[start:end+1])
    maxVal=max(arr[start:end+1])

    #check if minVal deserves a pos before start
    for i in range(start):
        if arr[i]<minVal:
            start=i
            break
     #check if maxVal deserves a pos after end
    for i in range(len(arr)-1,end,-1):
        if arr[i]>maxVal:
            end=i
            break

    return arr[start:end+1]

    
    
    
