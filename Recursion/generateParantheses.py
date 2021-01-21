'''
leetcode 22  Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''
li=[]
global n
n=3
def helper(s,openb,closeb):
    if openb==n and closeb==n:
        li.append(s)

    if openb<n:
        helper(s+'(',openb+1,closeb)
    if closeb<openb:
        helper(s+')',openb,closeb+1)

helper("",0,0)
print(li)