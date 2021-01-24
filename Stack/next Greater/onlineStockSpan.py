'''
online stock span

The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days.
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}

'''
#approach 1
def fun(arr):
    stack=[]
    result=[]

    for i in range(len(arr)):
        if len(stack)==0:
            result.append(1)
            stack.append([i,1])
        else:
            while stack and arr[i]>=stack[-1][1]:
                stack.pop()
            if len(stack)==0:
                result.append(1)
            else:
                result.append(i-stack[-1][0])
        
        stack.append([i,arr[i]])
    
    print(result)

#efficient approach
#Finacial Problem in Dholokpur
def fun2(arr):
    st=[]
    res=[]
    for i in range(len(arr)):
        #print(st)
        while st and arr[st[-1]]<arr[i]:
            st.pop()
        if st:
            res.append(i-st[-1])
        else:
            res.append(i+1)

        st.append(i)
    print(res)
fun2([100,80,60,70,60,75,85])