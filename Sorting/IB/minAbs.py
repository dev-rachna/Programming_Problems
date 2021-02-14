
def fun(arr):
    mini=float('inf')
    arr.sort()
    for i in range(1,len(arr)):
        mini=min(mini,arr[i]-arr[i-1])
    
    return mini
    