'''
leetcode 986. Interval List Intersections
Given two lists of closed intervals, each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
'''

def intervalIntersection(A, B):
    a,b=0,0
    res=[]
    while a<len(A) and b<len(B):
        s1,e1=A[a]
        s2,e2=B[b]

        if s1<=e2 and s2<=e1:
            res.append([max(s1,s2),min(e1,e2)])
        
        if e1>e2:
            b+=1
        else:
            a+=1
    print(res)


intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]])
