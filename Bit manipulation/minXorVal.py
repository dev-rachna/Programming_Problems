def fun(arr):
    arr.sort()
    mini=float('inf')
    for i in range(1,len(arr)):
        mini=min(mini,arr[i]^arr[i-1])
    return mini
