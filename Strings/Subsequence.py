# -*- coding: utf-8 -*-

'''
Given two strings str1 and str2, find if str1 is a subsequence of str2.
'''

def subsequence(s1,s2):   
    i=0
    j=0
    while j<len(s1) and i<len(s2):
        if s1[j]==s2[i]:
            j+=1
        i+=1
    
    if j==len(s1):
        print('true')
    else:
        print('false')
        
subsequence("ABY", "ADXCPY")

        
        
    