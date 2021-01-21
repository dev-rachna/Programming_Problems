def merge(left,right,A):
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            A[k]=left[i]
            i+=1

        else:
            A[k]=right[j]
            j+=1
        k+=1
    
    while i<len(left):
        A[k]=left[i]
        i+=1
        k+=1
    
    while j<len(right):
        A[k]=right[j]
        j+=1
        k+=1
    

def mergesort(A):
    n=len(A)
    if n<2:
        return
    mid=n//2
    left=A[:mid]
    right=A[mid:]
    mergesort(left)
    mergesort(right)
    merge(left,right,A)

A=[2,1,-2,7,3]
mergesort(A)
print(A)

