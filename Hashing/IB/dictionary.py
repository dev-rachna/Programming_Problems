#naman hash 2 refer notes

def fun(string,dictionary):
    import collections
    frequency=collections.Counter(string)
    res=''
    for i in dictionary:
        if i in frequency:
            res+=i*frequency[i]
        
    return res

print(fun('aabfcade','cbfade'))



#Sort Array in given Order
#i/p: [1, 2, 3, 4, 5],[5, 4, 2]
#o/p:[5, 4, 2, 1, 3]

def fun2(A,B):
    #same as above
    pass