# -*- coding: utf-8 -*-


def threeSum(arr,target):
    arr.sort()
    res=[]
    #print(arr)
    for i in range(len(arr)-2):
        if i>0 and arr[i]==arr[i-1]:
            continue
        l=i+1
        r=len(arr)-1
        while l<r:
            #print(i,l,r)
            sm=arr[i]+arr[l]+arr[r]
            if sm==target:
                res.append([arr[i],arr[l],arr[r]])
                while l<r and arr[l]==arr[l+1]:
                    l+=1
                while l<r and arr[r]==arr[r-1]:
                    r-=1
                l+=1               
                r-=1      
            elif sm<target:
                l+=1
            
            else:
                r-=1     
    print(res)

threeSum([-2,-2,-3,-3,5,5,0],10)
