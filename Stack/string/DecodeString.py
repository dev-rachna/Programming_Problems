'''
394. Decode String
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

'''

def decodeString(s):
    stack=[]
    res=''
    num=0

    for i in s:
        if i=='[':
            stack.append(res)
            stack.append(num)
            num=0
            st=''
        elif i==']':
            j=stack.pop()
            string=stack.pop()
            st=string+st*j
            num=0
        elif i.isdigit():
            num=num*10+int(i)
        else:
            st+=i
    

