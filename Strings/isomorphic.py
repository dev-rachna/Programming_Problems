# -*- coding: utf-8 -*-

'''
Check if two given strings are isomorphic to each other
leetcode 205. Isomorphic Strings
'''

def isomorphic(a,b):
    if len(a)!=len(b):
        return -1
    m1=[0]*256 
    m2=[0]*256 
    
    print
    for i in range(len(a)):
        if m1[ord(a[i])]!=m2[ord(b[i])]:
            return -1
        #store where have you seen this before
        m1[ord(a[i])]=i+1
        m2[ord(b[i])]=i+1
    return True
    
print(isomorphic("egg","add"))