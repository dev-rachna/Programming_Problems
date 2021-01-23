#refer notes
'''
l,r always valid (pepcoding)
'''
def fun(arr,l,r):
    xor=[]
    curr_xor=0
    for i in arr:
        curr_xor^=i
        xor.append(curr_xor)
    
    if l==0:
        return xor[r]
    else:
        return xor[r]^xor[l-1]

print(fun([3,2,4],1,2))