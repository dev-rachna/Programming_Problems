# -*- coding: utf-8 -*-
'''
Given two strings in lowercase, the task is to make them anagram.
  The only allowed operation is to remove a character from any string.
  Find minimum number of characters to be deleted to make both the strings anagram?
  
  '''
  
import collections
  
def minDelAnagram(s1,s2):
    res=0
    count=collections.Counter(s1)    
    for i in s2:
        count[i]-=1    
    for i in count:
        res+=abs(count[i])    
    print(res)
        

minDelAnagram("abcd","cab")   
      