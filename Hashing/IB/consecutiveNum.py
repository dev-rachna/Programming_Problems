#naman hash 2 refer notes

def fun(arr):
    set1=set(arr)
    maxi=0
    for i in arr:
        if i-1 not in set1:
            count=1
            while i+1 in set1:
                count+=1
                i+=1
        maxi=max(maxi,count)
    return maxi    
