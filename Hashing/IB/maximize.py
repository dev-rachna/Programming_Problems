'''
refer notes for problem statement
'''
#maximize
def fun(arr):
    first_occurance={}
    maxi=0
    for i in range(len(arr)):
        if arr[i] not in first_occurance:
            first_occurance[arr[i]]=i
        else:
            maxi=max(maxi,i-first_occurance[arr[i]])
    return maxi


#minimize
def fun2(arr):
    last_occurance={}
    mini=float('inf')
    for i in range(len(arr)):
        if arr[i]  in last_occurance:
            mini=min(mini,i-last_occurance[arr[i]])
           
        last_occurance[arr[i]]=i
    if mini==float('inf'):
        return "all distinct ele"
            