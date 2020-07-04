# -*- coding: utf-8 -*-

'''
Leetcode 14
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
'''

def longestCommonPrefix(strs):
    

    prefix=""
    for i in range(len(strs[0])):
        for j in range(len(strs)):
            if strs[j][i]!=strs[0][i]:
                return prefix
                
        prefix+=strs[0][i]   
                

    return prefix

print(longestCommonPrefix(["aa","aa"]))