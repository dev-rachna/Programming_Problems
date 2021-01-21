def insertionsort(A):
    for i in range(1,len(A)):
        val=A[i]
        pivot=i
        while pivot>0 and A[pivot-1]>val:
            A[pivot]=A[pivot-1]
            pivot-=1
        A[pivot]=val
    print(A)

insertionsort([9,4,3,1,18,35])