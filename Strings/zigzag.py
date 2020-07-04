# -*- coding: utf-8 -*-

'''
leetcode 6. ZigZag Conversion
'''

import collections

def zigzag(s,rows):
    
    mydict=collections.defaultdict(list)
    pos=0
    inc=True
    for i in range(len(s)):
        if pos==rows:
            inc=False
        elif pos==1:
            inc=True
            
        if inc:
            pos+=1
        else:
            pos-=1
        
        mydict[pos].append(s[i])
    res=''
    for i in range(1,rows+1):
        res+=''.join(mydict[i])
        
    print(res)
zigzag("PAYPALISHIRING",3)