# -*- coding: utf-8 -*-

'''
leetcode 678. Valid Parenthesis String

'''
#store position because **( will always be false
def validPara(s):
    star=[]
    opBracket=[]
    
    for i in range(len(s)):
        if s[i]=='*':
            star.append(i)
        elif s[i]=='(':
            opBracket.append(i)
        else:
            if opBracket:
                opBracket.pop()
            elif star:
                star.pop()
            else:
                return False
    
    #if still there are open brackets
    while opBracket:
        if star and opBracket[-1]>star[-1]:
            return False
        elif len(star)==0:
            return False
        else:
            opBracket.pop()
            star.pop()
    return True

print(validPara('**(()'))