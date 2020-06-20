# -*- coding: utf-8 -*-


from lcs import lcs

def shortestCommonSuperSequence(s1,s2): 
    print('length= ',len(s1)+len(s2)-lcs(s1,s2))

shortestCommonSuperSequence("AGGTAB","GXTXAYB")
    