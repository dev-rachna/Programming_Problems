'''
763. Partition Labels

A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
 

Note:

S will have length in range [1, 500].
S will consist of lowercase English letters ('a' to 'z') only.

'''
import collections
def partitionLabels(s):
    last_index=collections.defaultdict(int)

    for i in range(len(s)):
        last_index[s[i]]=i
    

    left=0
    right=0
    result=[]
    for i in range(len(s)):

        right=max(right,last_index[s[i]])

        if i==right:
            result.append(right-left+1)
            left=i+1

    
    return result


