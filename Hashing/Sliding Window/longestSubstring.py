'''
3. Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

def fun(s):
    mapping={}
    start=0
    maxlen=0

    for i in range(len(s)):

        if s[i] in mapping and start<=mapping[s[i]]:
            start=mapping[s[i]]+1
        else:
            maxlen=max(maxlen,i-start+1)
        mapping[s[i]]=i
    return maxlen

print(fun("dvdf"))
