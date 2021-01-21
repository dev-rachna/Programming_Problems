'''
354. Russian Doll Envelopes

You have a number of envelopes with widths and heights given as a pair of integers (w, h).
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.

What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note:
Rotation is not allowed.

Example:

Input: [[5,4],[6,4],[6,7],[2,3]]
Output: 3 
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

'''

def maxEnvelopes(envelopes):
    envelopes.sort()

    dp=[1 for i in range(len(envelopes))]

    for i in range(len(envelopes)):
        for j in range(i):
            if envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1] and dp[i]<=dp[j] :
                dp[i]=dp[j]+1
    
    return max(dp)


print(maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))

