'''
leetcode 56. Merge Intervals
Given a collection of intervals, merge all overlapping intervals
'''

def merge(intervals):

    intervals.sort()
    res=[intervals[0]]

    for i in range(1,len(intervals)):
        if intervals[i][0]<res[-1][1]:
            res[-1][1]=max(intervals[i][1],res[-1][1])
        else:
            res.append(intervals[i])

    return res


print(merge([[1,3],[2,6],[8,10],[15,18]]))