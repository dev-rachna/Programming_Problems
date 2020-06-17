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
        
    # 19. Remove Nth Node From End of List leetcode
    def removeNthFromEnd(self,n):
        #Assume n to be valid
        res=self.head
        slow=res
        fast=res
        
        i=1
        while i!=n+1:
            fast=fast.next
            i+=1
        # print(fast.val)
        if fast is None:
            return res.next
        while fast.next:
            slow=slow.next
            fast=fast.next
        # print(slow.val)
        slow.next=slow.next.next
        return res
    
    # 876. Middle of the Linked List
    def middleNode(self):
        if not (self.head or self.head.next):
            print('empty list')
            return
        
        slow=self.head
        fast=self.head
        
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.val)
    
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
head=list1.removeNthFromEnd(1)
printList(head)
list1.middleNode()
