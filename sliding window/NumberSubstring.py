'''
1358. Number of Substrings Containing All Three Characters

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
Example 3:

Input: s = "abc"
Output: 1

'''

def fun(s):
    count={'a':0,'b':0,'c':0}

    result=0
    left=0

    for right in range(len(s)):
        count[s[right]]+=1
        
        while count['a']>0 and count['b']>0 and count['c']>0:
            result+=len(s)-right
            count[s[left]]-=1
            left+=1
        
    
    return result