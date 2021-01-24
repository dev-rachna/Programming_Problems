'''

'''

def fun(arr,k):
    last=sum(arr[len(arr)-k:])
    maxi=0
    first=0
    for i in range(k):
        first+=arr[i]
        last-=arr[len(arr)-k+i]
        maxi=max(maxi,first+last)
    return maxi