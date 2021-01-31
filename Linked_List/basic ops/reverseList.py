# -*- coding: utf-8 -*-


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
    
    def reverseIter(self):
        if self.head is None:
            print('empty list')
            return
        curr=self.head
        prev=None
        
        while curr:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        self.head=prev
    
    def reverseRecursive(self,root):
        if root.next is None:
            self.head=root
            return
        self.reverseRecursive(root.next)
        q=root.next
        q.next=root
        root.next=None
        
        
    def printList(self):
        if self.head is None:
            print('empty list')
        curr=self.head
        while curr:
            print(curr.val)
            curr=curr.next

list1=LinkedList()  
list1.insertEnd(Node(1))
list1.insertEnd(Node(2))
list1.insertEnd(Node(3))
list1.insertEnd(Node(4))
list1.insertEnd(Node(5))
list1.insertEnd(Node(6))
# list1.reverseIter()
list1.reverseRecursive(list1.head)
list1.printList()
        
        
        
        
            
            
        
