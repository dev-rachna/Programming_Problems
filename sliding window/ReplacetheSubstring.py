'''
1234. Replace the Substring for Balanced String

You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.
A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.
Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced.
Return 0 if the string is already balanced.

 

Example 1:

Input: s = "QWER"
Output: 0
Explanation: s is already balanced.
Example 2:

Input: s = "QQWE"
Output: 1
Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.
Example 3:

Input: s = "QQQW"
Output: 2
Explanation: We can replace the first "QQ" to "ER". 
Example 4:

Input: s = "QQQQ"
Output: 3
Explanation: We can replace the last 3 'Q' to make s = "QWER".
'''
import collections
def fun(s):
    count=collections.Counter(s)

    for i in count:
        count[i]=max(0,count[i]-len(s)//4)
    
    left=0
    minlen=float('inf')

    for right in range(len(s)):
        count[s[right]]-=1

        while left<len(s) and count['Q']<=0 and count['W']<=0 and count['E']<=0 and count['R']<=0:
            count[s[left]]+=1
            minlen=min(minlen,right-left+1)
            left+=1
        
    
    return minlen


    

