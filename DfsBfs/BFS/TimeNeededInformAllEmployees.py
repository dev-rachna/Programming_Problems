'''
leetcode 1376. Time Needed to Inform All Employees
'''

import collections


def bfs(mapping, informTime):

    time = 0
    que = collections.deque()
    que.append([-1, 0])
    maxi = 0
    while que:
        temp = que.popleft()
        for i in mapping[temp[0]]:
            time = temp[1]+informTime[i]
            que.append([i, time])
            maxi = max(maxi, temp[1]+informTime[i])

    return(maxi)


def numOfMinutes(n, headID, manager, informTime):
    """
    :type n: int
    :type headID: int
    :type manager: List[int]
    :type informTime: List[int]
    :rtype: int
    """

    mapping = collections.defaultdict(list)

    for i in range(len(manager)):
        mapping[manager[i]].append(i)

    return bfs(mapping, informTime)


print(numOfMinutes(7,6,[1,2,3,4,5,6,-1],[0,6,5,4,3,2,1]))