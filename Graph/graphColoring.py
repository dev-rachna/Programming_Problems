# -*- coding: utf-8 -*-

'''
leetcode 886. Possible Bipartition
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group. 

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.
'''

import collections

def bipartite(i,mapping,colored):
    colored[i]=1
    que=collections.deque()
    que.append(i)
    while que:      
        curr=que.popleft()
        for j in mapping[curr]:            
            if colored[j]==colored[curr]:
                return False
            if colored[j]==-1:
                colored[j]=1-colored[curr]
                que.append(j)                
    return True
    
def possibleBipartition(N, dislikes):   
    dis_mapping=collections.defaultdict(list)
    colored=[-1 for i in range(N+1)]
    for a,b in dislikes:
        dis_mapping[a].append(b)
        dis_mapping[b].append(a)
    # print(dis_mapping)   
    for i in range(1,N+1):        
        if colored[i]==-1 and not bipartite(i,dis_mapping,colored):
            
            return False
    
    return True

print(possibleBipartition(3,  [[1,2],[1,3],[2,3]]))