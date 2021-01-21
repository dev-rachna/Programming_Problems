'''
leetcode 875. Koko Eating Bananas
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.
Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.
Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.
Return the minimum integer K such that she can eat all the bananas within H hours.
'''

def isValid(piles,H,mid):
    k=0

    for i in piles:
        k+=i//mid
        if i%mid!=0:
            k+=1
    return k


   

def minEatingSpeed(piles, H):
    low=1
    high=max(piles)

    while low<=high:
        mid=(low+high)//2
        k=isValid(piles,H,mid)
        # print(k,mid)
        if k<=H:
            high=mid-1
        else:
            low=mid+1
        
        # print(low,high)
        
    return low

print(minEatingSpeed([3,6,7,11],8))

