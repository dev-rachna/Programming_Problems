def partition(A,start,end):
    pivot=A[end]
    partitionIndex=start
    for i in range(start,end):
        if A[i]<=pivot:
            A[partitionIndex],A[i]=A[i],A[partitionIndex]
            partitionIndex+=1
    
    A[partitionIndex],A[end]=A[end],A[partitionIndex]
    return partitionIndex

    
def quicksort(A,start,end):
    if start<end:
        pivot_index=partition(A,start,end)
        quicksort(A,start,pivot_index-1)
        quicksort(A,pivot_index+1,end)

A=[4,2,6,1,7]
quicksort(A,0,len(A)-1)
print(A)