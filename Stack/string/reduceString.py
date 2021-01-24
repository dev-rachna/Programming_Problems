'''
i/p:aaabccddd
o/p:abd
'''
def fun(s):
    st=[]
    for i in s:
        if st and st[-1]==i:
            st.pop()
        else:
            st.append(i)
    return ''.join(st)