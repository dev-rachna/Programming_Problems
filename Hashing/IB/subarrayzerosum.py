'''
longest subarray with zero sum
'''

def fun(arr):
    #entire arr sum might be zero
    count={0:0}
    curr_sm=0
    maxi=0
    for i in range(len(arr)):
        curr_sm+=arr[i]

        if curr_sm in count:
            maxi=max(maxi,i-count[curr_sm]+1)
        #care about first occ
        else:
            count[curr_sm]=i
    return maxi

