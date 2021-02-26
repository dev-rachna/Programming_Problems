# -*- coding: utf-8 -*-
# edge self loop
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertEnd(self,node):
        if self.head is None:
            self.head=node
            
        curr=self.head
        while curr.next:
            curr=curr.next        
        curr.next=node
        node.next=None
        
    #Assume there is a loop
    def cycleDetection(self):
        slow=self.head
        fast=self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                print('loop detetced')
                return
        print('no loop')
        return 
    
    def detectStartOfLoop(self):
        slow=self.head
        fast=self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                slow=self.head
                while fast!=slow: #fast.next!=slow.next remove loop
                    slow=slow.next
                    fast=fast.next
                print(slow.val)
                # fast.next=None remove loop
                return
        print('No loop')
        return
    
    def countLengthOfLoop(self):
        slow=self.head
        fast=self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            
            if slow==fast:
                count=1
                slow=slow.next
                while fast!=slow:
                    slow=slow.next
                    count+=1
                print('length of loop is ',count)
                return
        print('No loop')
        return

list1=LinkedList()  
list1.insertEnd(Node(1))
list1.insertEnd(Node(2))
list1.insertEnd(Node(3))
list1.insertEnd(Node(4))
list1.insertEnd(Node(5))
list1.insertEnd(Node(6))
#make loop
list1.head.next.next.next.next.next=list1.head.next.next

list1.cycleDetection()
list1.detectStartOfLoop()
list1.countLengthOfLoop()
