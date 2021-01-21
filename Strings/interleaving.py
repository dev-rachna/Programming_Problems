# -*- coding: utf-8 -*-
'''
Given three strings A, B and C. 
Write a function that checks whether C is an interleaving of A and B.
 It may be assumed that there is no common character between A and B.
 C is said to be interleaving A and B, if it contains all characters of A and B and order of all characters in individual strings is preserved.
 Ex.
 str1 = "AB",  str2 = "CD"
 c=ABCD
 
 o/p:yes
'''

def interleaving(A,B,C):
    i=0
    j=0
    k=0
    while i<len(C):
        if j<len(A) and C[i]==A[j]:
            j+=1
        elif k<len(B) and C[i]==B[k]:
            k+=1
        else:
            return False
        
        i+=1
    
    return True
        
print(interleaving("AAB","AXY","AABAXY"))
        


'''
Given two strings str1 and str2, write a function that prints all interleavings of the given two strings.
 You may assume that all characters in both strings are different

'''


def printInterleaving(a,b,m,n,res,i):
    # print(a,b,m,n,res,i)
    
    if m==0 and n==0:
        print('res',res)
        
    if m!=0:
        res[i]=a[0]
        printInterleaving(a[1:],b,m-1,n,res,i+1)
    
    if n!=0:
        res[i]=b[0]
        printInterleaving(a,b[1:],m,n-1,res,i+1)

a="AB"
b="CD"
li=['']*(len(a)+len(b))
printInterleaving(a,b,len(a),len(b),li,0)        
        

    