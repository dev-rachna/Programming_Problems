'''
leetcode 179. Largest Number
Given a list of non negative integers, arrange them such that they form the largest number.
'''


def largestNumber(arr):
   

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if str(arr[i])+str(arr[j]) < str(arr[j])+str(arr[i]):
                arr[i],arr[j]=arr[j],arr[i]

    print(arr)


largestNumber([8,89])