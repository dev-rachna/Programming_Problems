'''
leetcode 1288. Remove Covered Intervals
Given a list of intervals, remove all intervals that are covered by another interval in the list.
 Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
After doing so, return the number of remaining intervals.
'''

def removeCoveredIntervals(intervals):
    intervals.sort()

    c,d=intervals[0]
    res=0
    i=1
    while i<len(intervals):
        a,b=intervals[i]
        if c<=a and b<=d:
            res+=1
        else:
            c,d=a,b
        i+=1
    print(res)
    print(len(intervals)-res)


removeCoveredIntervals([[1,4],[3,6],[2,8]])