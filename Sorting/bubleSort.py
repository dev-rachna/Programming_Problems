
def bubbleSort(A):
    for i in range(len(A)-1):
        flag=0
        for j in range(0,len(A)-1-i):
            if A[j]>A[j+1]:
                flag=1
                A[j],A[j+1]=A[j+1],A[j]
        if flag==0:
            break
    print(A)


bubbleSort([4,3,68,1])
