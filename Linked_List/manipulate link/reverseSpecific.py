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



def reverseSpecific(head,m,n):
    if m==n:
        print('no need to reverse')
        return
    node=Node(0)
    node.next=head
    prev=node
    for _ in range(m-1):
        prev=prev.next
    
    reverse=None
    curr=prev.next
    for _ in range(n-m+1):
        next1=curr.next
        curr.next=reverse
        reverse=curr
        curr=next1
    
    prev.next.next=curr
    prev.next=reverse
    
    return node.next
    
    
def printList(head):
        if head is None:
            print('empty list')
        curr=head
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

head=reverseSpecific(list1.head,2,4)
printList(head)