def fun(num):
    res=0

    for i in range(32):
        bit=(num>>i)&1
        shift_left=bit<<(31-i)
        res=res|shift_left
    return res