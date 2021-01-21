def fun(arr):
    majority=arr[0]
    count=0

    for i in range(len(arr)):
        if arr[i]==majority:
            count+=1
        else:
            count-=1
            if count==0:
                majority=arr[i]
    
    return majority
