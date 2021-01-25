# naman hash 2 refer notes


#math based
def fun(arr):
    import collections
    frequency=collections.Counter(arr)
    count=0
    for i in frequency:
        count+=(frequency[i]*(frequency[i]-1)//2)
    return count

#without math optimized
def fun2(arr):
    frequency={}
    count=0
    for i in arr:
        if i in frequency:
            count+=frequency[i]
            frequency[i]+=1
        else:
            frequency[i]=1
    return count

