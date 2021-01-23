'''
every no twice and one no once
'''
def fun(arr):
    xor=0
    for i in arr:
        xor^=i
    return xor


'''
every no twice and 2 number ones
'''
def fun2(arr):
    xor=0
    for i in arr:
        xor^=i
    mask=xor^(xor&(xor-1))
    xor1=0
    xor2=0
    for i in arr:
        if mask&i>0:
            xor1^=i
        else:
            xor2^=i
    
    print(xor1,xor2)

fun2([2,3,5,5,3,4])

