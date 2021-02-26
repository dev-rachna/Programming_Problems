import math
# max heap

def heapify(A, i):
    L = 2*i+1
    R = 2*i+2
    largest = -1
    if L < len(A) and A[L] > A[i]:
        largest = L
    else:
        largest = i
    if R < len(A) and A[R] > A[largest]:
        largest = R

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        heapify(A, largest)


def buildHeap(A):
    end = math.floor(len(A))-1
    for i in range(end, -1, -1):
        heapify(A, i)
    print(A)
    return A

def increaseKey(A,i,key):
    if key<A[i]:
        A[i]=key
        heapify(A,i)
    else:
        A[i]=key
        while i>0 and A[math.ceil(i/2)-1]<A[i]:
            A[math.ceil(i/2)-1],A[i]=A[i],A[math.ceil(i/2)-1]
            i=math.ceil(i/2)-1


def getMax(A):
    maxi=A[0]
    A[0]=A.pop()
    heapify(A,0)
    print(maxi)

def insertElement(A,key):
    A.append(key)
    i=len(A)-1
    while i>0 and A[math.ceil(i/2)-1]<A[i]:
        A[math.ceil(i/2)-1],A[i]=A[i],A[math.ceil(i/2)-1]
        i=math.ceil(i/2)-1




A=buildHeap([10,9,11,2,3,5])
increaseKey(A,4,1)
print(A)
getMax(A)
print(A)
insertElement(A,12)
print(A)