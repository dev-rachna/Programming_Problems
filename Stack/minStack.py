'''
Design a data structure that performs the following operation in O(1) time on a stack

1.push()
2.pop()
3.top()
4.getMin()

'''
class minStack:
    def __init__(self):
        self.stack=[]
        self.min=float('inf')
        
    def push(self,val):
        if len(self.stack)==0:
            self.stack.append(val)
            self.min=val

        elif self.stack and self.min>val:
            self.stack.append(2*val-self.min)
            self.min=val
        else:
            self.stack.append(val)
            
    def pop1(self):
        if len(self.stack)==0:
            return -1
        
        elif self.stack[-1]<self.min:
            self.min=2*self.min-self.stack.pop()
        else:
            self.stack.pop()

    def top(self):
        if len(self.stack)==0:
            return -1
        
        if self.stack[-1]<=self.min:
            print(self.stack)
            return self.min
        else:
            return self.stack[-1]
        

    def getMin(self):
        return self.min


ms=minStack()
ms.push(10)
ms.push(6)
ms.push(5)
print(ms.top())
print(ms.getMin())
ms.pop1()
print(ms.top())
ms.pop1()
print(ms.getMin())