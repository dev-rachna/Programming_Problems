#approach 1
def fun(arr,k):
    return sorted(arr)[k]

#approach 2 O(kn)
#k<500 and N-10^6
def fun2(arr,k):

    for i in range(k+1):
        minI=i
        for j in range(i+1,len(arr)):
            if arr[minI]>arr[j]:
                minI=j
        arr[minI],arr[i]=arr[i],arr[minI]

    return arr[k]

#otherwise heap sort O(nlog(K))