def fun(num):
    count=0
    while num>0:
        num=num&num-1
        count+=1
    return count

print(fun(4))

#power of 2
# (has only 1 set bit)
def fun2(num):
    if num&(num-1)==0:
        return 1
    return 0
