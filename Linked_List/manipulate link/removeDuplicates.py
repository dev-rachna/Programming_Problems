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
 

       
def removeDuplicatesSorted(head):   
    curr=head
    while curr and curr.next:
        if curr.val==curr.next.val:
            curr.next=curr.next.next
        else:
            curr=curr.next
    return head

#leetcode 82
def removeDuplicatesSorted2(head):
    curr=head
    prev=None
    while curr and curr.next:
        if curr.next==curr.next.val:
            while  curr.next==curr.next.val:
                curr=curr.next
            
            if curr==head:
                head=curr.next
            else:
                prev.next=curr.next
                curr=curr.next
        else:
            prev=curr
            curr=curr.next
    return head