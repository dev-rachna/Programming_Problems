def fun(arr):
    res=0
    count=0
    for i in range(32):
        count=0
        for element in arr:
            if (element>>i)&1==1:
                count+=1
        res=2*count*(len(arr)-count)
    return res