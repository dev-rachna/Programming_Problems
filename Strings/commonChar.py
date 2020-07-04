# -*- coding: utf-8 -*-

# Given two strings, print all the common characters in lexicographical order. 
# If there are no common letters, print -1. All letters are lower case.

import collections

def commonChar(s1,s2):
    s1char=collections.defaultdict(int)
    s2char=collections.defaultdict(int)
    
    res=''
    
    string="abcdefghijklmnopqrstuvwxyz"
    
    for i in s1:
        s1char[i]+=1
    
    for i in s2:
        s2char[i]+=1
    
    for i in string:
        if i in s1char and i in s2char:
            temp=i*(min(s1char[i],s2char[i]))
            res+=temp
            
    print(res)
        
commonChar("geeks","forgeeks")