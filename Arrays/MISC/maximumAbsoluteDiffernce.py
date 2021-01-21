'''
GFG/IB
Given an unsorted array A of N integers, A_{1}, A_{2}, ...., A_{N}. Return maximum value of f(i, j) for all 1 ≤ i, j ≤ N.
f(i, j) or absolute difference of two elements of an array A is defined as |A[i] – A[j]| + |i – j|, where |A| denotes
the absolute value of A.

Aryan mittal

'''

def solve(arr):

    max1=float('-inf')
    max2=float('-inf')

    min1=float('inf')
    min2=float('inf')


    for i in range(len(arr)):

        max1=max(max1,arr[i]+i)
        max2=max(max2,arr[i]-i)
        min1=min(min1,arr[i]+i)
        min2=min(min2,arr[i]-i)
    return max(max1 - min1, max2 - min2)

array = [ -70, -64, -6, -56, 64, 61, -57, 16, 48, -98 ] 
  
print(solve(array))