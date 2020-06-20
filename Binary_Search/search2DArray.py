# -*- coding: utf-8 -*-
# Author:Rachna Devasthali

def search(matrix,key):    
    i=0
    j=len(matrix[0])-1
    while 0<=i<len(matrix) and 0<=j<len(matrix[0]):
        if matrix[i][j]==key:
            print('found')
            return
        elif matrix[i][j]<key:
            i+=1
        else:
            j-=1
    print('not found')
    
search([[11,12,13],[14,15,16],[17,18,19]],10)