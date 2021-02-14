'''
1011. Capacity To Ship Packages Within D Days
A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.
'''

def isValid(weights,D,mid):
    days=1
    capacity=0

    for i in range(len(weights)):
        capacity+=weights[i]
        # print('i',i,capacity)
        if capacity>mid:
            days+=1
            capacity=weights[i]
            
        if days>D:
            return False
        
    
    
    return True


def shipWithinDays(weights, D):
    res=-1
    low=max(weights)
    high=sum(weights)
    # print(low,high)
    while low<=high:
        mid=(low+high)//2
        # print('mid',mid)
        if isValid(weights,D,mid)==True:

            res=mid
            high=mid-1
            # print('res',res,high)
        else:
            low=mid+1

    return res

print(shipWithinDays([1,2,3,4,5,6,7,8,9,10],5))
