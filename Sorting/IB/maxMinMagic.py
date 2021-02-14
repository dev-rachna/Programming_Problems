def fun(arr):
    maxi=0
    mini=0

    for i in range(1,len(arr),2):
        mini+=abs(arr[i]-arr[i-1])%(10**9+7)
    
    for i in range(0,len(arr),2):
        maxi+=abs(arr[i]-arr[len(arr)-i-1])%(10**9+7)
    
    return (maxi,mini)
