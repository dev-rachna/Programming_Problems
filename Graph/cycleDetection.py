# -*- coding: utf-8 -*-

'''
leetcode 207. Course Schedule
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
'''

import collections
def detectCycle(i,mapping,visited):
    print(i,visited[i],mapping[i],visited)
    if visited[i]=="visiting":
        return True
    
    if visited[i]=="visited":
        return False
    
    visited[i]="visiting"
    for i in mapping[i]:
        # print(i,visited[i],mapping[i],visited,'2',print(detectCycle(i, mapping, visited)))
        if detectCycle(i, mapping, visited):
            return False
    visited[i]="visited"
    return True

def canFinish(numCourses, prerequisites):
    pre_req_mapping=collections.defaultdict(list)
    visited=["not_visited" for i in range(numCourses)]
    
    for i in prerequisites:
        pre_req_mapping[i[0]].append(i[1])
    print(pre_req_mapping)
    for i in range(numCourses):
        if  detectCycle(i,pre_req_mapping,visited):
            return False
    return True


print(canFinish(2,[[1,0]])) 