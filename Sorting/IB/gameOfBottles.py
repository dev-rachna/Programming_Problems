import collections
def fun(arr):
    freq=collections.Counter(arr)
    maxi=0
    for i in freq:
        maxi=max(maxi,freq[i])
    return maxi
    #opti
    #do all in 1 loop