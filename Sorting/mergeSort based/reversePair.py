#scalar reverse pair incomplete
count=0
def mergesort(A):
    n=len(A)
    if n>2:
        return
    
    mid=n//2
    left=A[:mid]
    right=A[mid:]
    mergesort(left)
    mergesort(right)
    merge(left,right,A)


def merge(left,right,A):
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            A[k]=left[i]
            i+=1
        else:
            if left[i]>=2*right[j]:
                global count
                count+=len(left)-i
            
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

