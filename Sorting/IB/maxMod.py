#approach 1
def fun(arr):
    maxi=0
    arr.sort()
    for i in range(1,len(arr)):
        maxi=max(maxi,arr[i-1]%arr[i])
    
    return maxi

#approach 2
'''
1,2,3,3  if smax==fmax the ans would be min so make sure the cond is never attained.
'''

def fun2(arr):
    fmax=0
    smax=0

    for i in range(len(arr)):
        if arr[i]>fmax:
            smax=fmax
            fmax=arr[i]
        elif arr[i]>smax and arr[i]!=fmax:
            smax=arr[i]
    return smax%fmax
