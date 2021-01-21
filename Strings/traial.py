def fun(A):
    l1=0
    A1=set(A)
    while len(A)!=l1:
        l1=len(A)
        for i in range(len(A)):
            for j in range(i+1,len(A)):
                temp=abs(A[i]-A[j])
                if temp not in A1 and temp!=0:
                    A1.add(temp)
                    A.append(temp)
        

    print(A1)
    print(len(A1))


def find_gcd(x, y): 
    while(y): 
        x, y = y, x % y 
  
    return x 
      
      
l = [] 
  
num1=l[0] 
num2=l[1] 
gcd=find_gcd(num1,num2) 
  
for i in range(2,len(l)): 
    gcd=find_gcd(gcd,l[i]) 
      
print(gcd) 

#fun([6,8,6,12,15,24,27] )