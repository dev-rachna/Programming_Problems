'''
171. Excel Sheet Column Number
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:
Input: "A"
Output: 1
Example 2:
Input: "AB"
Output: 28
Example 3:
Input: "ZY"
Output: 701
 
Constraints:
1 <= s.length <= 7
s consists only of uppercase English letters.
s is between "A" and "FXSHRXW".
'''
import collections
def titleToNumber(s):
    string=' ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mapping=collections.defaultdict(int)
    for i in range(len(string)):
        mapping[string[i]]=i
    
    power=len(s)-1
    res=0
    for i in range(len(s)):
        res+=mapping[s[i]]*(26**power)
        power-=1
    
    return res

def convertToTitle(n):
    string='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result=''
    while n:
        result+=string[(n-1)%26]
        n=(n-1)//26
    
    return result


# print(titleToNumber('A'))
print(convertToTitle(701))
        

