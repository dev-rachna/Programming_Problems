def fun(arr):
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if str(arr[i])+str(arr[j])<str(arr[j])+str(arr[i]):
                arr[i],arr[j]=arr[j],arr[i]
    return ''.join(arr)