# -*- coding: utf-8 -*-

class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertBegin(self,node):      
        if self.head is None:            
            self.head=node           
            return
        
        node.next=self.head
        self.head=node
        
    
    def insertEnd(self,node):
        if self.head is None:
            self.head=node
            
        curr=self.head
        while curr.next:
            curr=curr.next        
        curr.next=node
        node.next=None
    
    def insertMiddle(self,node,pos):
        #Assume list is non-empty
        #and pos is valid 
        if pos==1:
            self.insertBegin(node)
            return
        curr=self.head
        prev=curr
        i=1
        while i!=pos:
            prev=curr
            curr=curr.next
            i+=1
        
        prev.next=node
        node.next=curr
        
        
    ##_____________Delete________________________
    def delBegin(self):
        if self.head is None:
            print('empty list')
            return
        temp=self.head
        self.head=self.head.next
        del(temp)
    
    def delEnd(self): 
        if self.head is None:
            
            print('empty list')
            return
        curr=self.head
        while curr.next.next:
            curr=curr.next
        
        temp=curr.next
        curr.next=None
        del(temp)
    
    def delMiddle(self,pos):
        #assume list non-empty and pos to be valid
        if pos==1:
            self.delBeg()
        curr=self.head
        prev=None
        i=1
        while pos!=i:
            prev=curr
            curr=curr.next
            i+=1
        prev.next=curr.next
        del(curr)
        
    
    def printList(self):
        if self.head is None:
            print('empty list')
        curr=self.head
        while curr:
            print(curr.val)
            curr=curr.next
  
list1=LinkedList()  
list1.insertBegin(Node(1)) 
list1.insertBegin(Node(2)) 
list1.insertBegin(Node(3)) 
list1.insertEnd(Node(4))
list1.insertMiddle(Node(5),1)
list1.insertMiddle(Node(6),2)
list1.delBegin()
list1.printList()
print('-----')
list1.delEnd()
list1.printList()
print('-----')
list1.delMiddle(3)
list1.printList()
            
        
        