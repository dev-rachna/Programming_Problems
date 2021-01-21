'''
Implement two stacks in an array
Create a data structure twoStacks that represents two stacks. Implementation of twoStacks should use only one array, i.e., both stacks should use the same array for storing elements. Following functions must be supported by twoStacks.
push1(int x) –> pushes x to first stack
push2(int x) –> pushes x to second stack

pop1() –> pops an element from first stack and return the popped element
pop2() –> pops an element from second stack and return the popped element

Implementation of twoStack should be space efficient.

'''
class twoStack:
    def __init__(self,size):
        self.stack=[0 for i in range(size)]
        self.top1=-1
        self.top2=len(self.stack)
    
    def push1(self,val):
        if self.top1+1<self.top2:
            self.stack[self.top1+1]=val
            self.top1+=1
        else:
            print('overflow')
    
    def push2(self,val):
        if self.top2-1>self.top1:
            self.stack[self.top2-1]=val
            self.top2-=1
        else:
            print('overflow')
    
    def pop1(self):
        if self.top1>=0:
            ele=self.stack[self.top1]
            self.top1-=1
            return ele
        else:
            return "empty"
    
    def pop2(self):
        if self.top2<len(self.stack):
            ele=self.stack[self.top2]
            self.top2+=1
            return ele
        else:
            return "empty"
    

stack1=twoStack(10)
stack1.push1(10)
stack1.push2(100)
stack1.push1(20)
stack1.push2(200)
stack1.push1(30)
stack1.push2(300)
stack1.push1(40)
stack1.push2(400)
stack1.push1(50)
stack1.push2(500)
print(
stack1.pop2(),stack1.push1(60))
print(stack1.stack)




