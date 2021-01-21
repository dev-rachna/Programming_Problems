def anti(A):
    res=[]
    for i in range(2*len(A)-1):
        li=[]
        

        if i<len(A):
            k=i
            for j in range(i+1):
                li.append(A[j][k])
                k-=1
            res.append(li)
        
        else:
            k=len(A)-1
            start=i-len(A)+1
            end=start+2*len(A)-i-1
            for j in range(start,end):
                print('i',j,i-len(A)+1)
                li.append(A[j][k])
                k-=1
            res.append(li)


    print(res)   

anti([[]])