
def selectionSort(A):
    end=len(A)-1
    ind=0
    for i in range(0,len(A)-2):
        ind=i
        for j in range(i+1,len(A)):
            if A[j]<A[ind]:
                ind=j
        A[i],A[ind]=A[ind],A[i]
    print(A)

selectionSort([4,2,1,6])