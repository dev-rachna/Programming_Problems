def fun(s1,s2):
    dp=[[False for i in range(len(s2)+1)] for _ in range(len(s1)+1)]
    #print(dp)
    dp[0][0]=True
    
    for i in range(1,len(s1)+1):
        if s1[i-1].islower():
            dp[i][0]=dp[i-1][0]
    
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1].isupper() and s1[i-1]==s2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            elif s1[i-1].isupper():
                dp[i][j]=False
            elif s1[i-1].islower() and s1[i-1].upper()==s2[j-1]:
                dp[i][j]=dp[i-1][j-1] or dp[i-1][j]
            elif s1[i-1].islower():
                dp[i][j]=dp[i-1][j]

                
    if dp[-1][-1]:
        print('YES')
    else:
        print('NO')
    
    

q=int(input())
for i in range(q):
    s1=input()
    s2=input()
    fun(s1,s2)

'''
2
daBcd
ABC
rACCEd
ACED
'''