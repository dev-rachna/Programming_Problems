# -*- coding: utf-8 -*-

'''
1410. HTML Entity Parser

'''

def entityParser(text):
    mapping={'&quot;':'"' ,'&apos;':'\'','&amp;':'&', '&gt;':'>','&lt;':'<','&frasl;':'/'}
    
    i=0
    res=''
    while i<len(text):
        
        if text[i]=='&':
            s=''
            while i<len(text):
                s+=text[i]
                
                if text[i]==';':
                    break
                else:
                    i+=1
                
                if text[i]=='&':
                    break
            if s in mapping:
                res+=mapping[s]
            else:
                res+=s
        else:
            res+=text[i]
        i+=1
    return res

print(entityParser("&amp; is an HTML entity but &ambassador; is not."))  