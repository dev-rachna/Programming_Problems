# -*- coding: utf-8 -*-

'''
leetcode 1309. Decrypt String from Alphabet to Integer Mapping
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 

'''

def freqAlphabets(s):
    letters=" abcdefghijklmnopqrstuvwxyz"
    mapping={}
    
    for i in range(1,27):
        if i>9:
            mapping[str(i)+'#']=letters[i]
        else:
            mapping[str(i)]=letters[i]
    # print(mapping)
    res=''
    i=0
    while i<len(s):
        
        if i+2<len(s) and s[i+2]=='#':
            
            res+=mapping[s[i:i+3]]
            i+=3
        else:
            res+=mapping[s[i]]
            i+=1
    print(res)
    

freqAlphabets('1326#')