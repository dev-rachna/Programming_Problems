#sign of int opp
def fun(num1,num2):
    if num1^num2>0:
        return True
    elif num1^num2<0:
        return False
    

#even odd
def fun2(num):
    if num&1>0:
        return "odd"
    return "even"


#unset i'th bit (i starts from zero)
def fun3(num,i):

    mask=1<<i
    return num&(~mask)


#set i'th bit (i starts from zero)
def fun4(num,i):
    mask=1<<i
    return num|mask

#toggle i'th bit
def fun5(num,i):
    mask=1<<i
    return num^mask

