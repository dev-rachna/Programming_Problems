#IB

def fun(arr):
    nsl=[]
    nsr=[0 for i in arr]
    ngl=[]
    ngr=[0 for i in arr]

    st_small=[]
    st_greater=[]
    for i in range(len(arr)):
        while st_small and arr[st_small[-1]]>=arr[i]:
            st_small.pop()
        
        if st_small:
            nsl.append(st_small[-1])
        else:
            nsl.append(-1)
        
        st_small.append(i)

        while st_greater and arr[st_greater[-1]]<=arr[i]:
            st_greater.pop()
        if st_greater:
            ngl.append(st_greater[-1])
        else:
            ngl.append(-1)
        
        st_greater.append(i)

    st_small=[]
    st_greater=[]
    for i in range(len(arr)-1,-1,-1):
        while st_small and arr[st_small[-1]]>=arr[i]:
            st_small.pop()
      
        if st_small:
            nsr[i]=st_small[-1]
        else:
            nsr[i]=len(arr)
        
        st_small.append(i)

        while st_greater and arr[st_greater[-1]]<=arr[i]:
            st_greater.pop()
        if st_greater:
            ngr[i]=st_greater[-1]
        else:
            ngr[i]=len(arr)
        
        st_greater.append(i)

    #print(nsr,nsl,ngr,ngl)

    curr_sum=0
    for i in range(len(arr)):
        curr_sum+=arr[i]*((ngr[i]-i)*(i-ngl[i])-(nsr[i]-i)*(i-nsl[i]))
        curr_sum%=(10**9+7)

    return curr_sum%(10**9+7)

print(fun([1,7,3,8]))