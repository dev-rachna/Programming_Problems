# -*- coding: utf-8 -*-

'''
leetcode 1417. Reformat The String

'''

def reformat(s):
    a=[]
    b=[]
    
    for i in s:
        if 'a'<=i<='z':
            a.append(i)
        else:
            b.append(i)
        
    if len(a)<len(b):
        a,b=b,a
    
    if len(a)-len(b)>=2:
        return -1
    ans=""
    for i in range(len(a)+len(b)):
        if i%2==0:
            ans+=a[i//2] # divisible by 2 so 0,1,2,3,4....
            
        else:
            ans+=b[i//2] # not divisible by 2 so 0,1,2,3,4....
           
    print(ans)


reformat("a0b1c2")
    