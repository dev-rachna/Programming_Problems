#fixed window

def fun(string,pattern):
    import collections
    st=collections.defaultdict(int)
    pt=collections.Counter(pattern)
    left=0
    count=0
    for right in range(len(string)):
        st[string[right]]+=1

        if right-left+1==len(pattern):
            if st==pt:
                count+=1
            st[string[left]]-=1
            if st[string[left]]<=0:
                st.pop(string[left])
            left+=1
    
    return count







