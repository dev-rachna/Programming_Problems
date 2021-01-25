#pepcoding

def fun(arr,k):
    remainder={}
    for i in arr:
        if i%k in remainder:
            remainder[i%k]+=1
        else:
            remainder[i%k]=1
    

    for i in remainder:
        if i==0:
            count+=remainder[i]//2

        elif 2*i==k:
            count+=remainder[i]//2
        else:
            if k-i in remainder:
                count+=remainder[i]*remainder[k-i]
    
    return count