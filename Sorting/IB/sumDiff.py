

def fun(arr):
    arr.sort()
    n=len(arr)
    min=0
    max=0
    for i in range(len(arr)):
        min+=2**(n-1-i)*arr[i]
    for i in range(len(arr)-1,-1,-1):
        max+=2**(i)*arr[i]
    return max-min
