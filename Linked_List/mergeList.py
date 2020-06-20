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
        return self.head


def sortList(head):
    if head is None or head.next is None:
        return head
    slow=head
    fast=head
    curr=head
    
    while fast and fast.next:
        curr=slow
        slow=slow.next
        fast=fast.next.next
    curr.next=None
    
    print(curr.val)
    print(slow.val)
    
    left=sortList(head)
    right=sortList(slow)
    head1=merge(left,right)
    printList(head1)



def merge(l1,l2):
    res=LinkedList()
    hd=res.insertEnd(Node(-1))
    # hd=hd.next
    curr=hd
    
    while l1 and l2:
        if l1.val<l2.val:
            hd.next=l1
            l1=l1.next
        else:
            hd.next=l2
            l2=l2.next
        hd=hd.next
    
    while l1:
        hd.next=l1
        l1=l1.next
        hd=hd.next
        
    while l2:
        hd.next=l2
        l2=l2.next
        hd=hd.next
    
    return curr.next
        
def printList(head):
     if head is None:
         print('empty list')
     curr=head
     while curr:
         print(curr.val)
         curr=curr.next

list1=LinkedList()  
list1.insertEnd(Node(1))
list1.insertEnd(Node(30))
list1.insertEnd(Node(9))
list1.insertEnd(Node(140))
list1.insertEnd(Node(15))
list1.insertEnd(Node(200))
list1.insertEnd(Node(21))
list1.insertEnd(Node(220))
head1=list1.insertEnd(Node(61))
sortList(head1)
# printList(head1)

# list2=LinkedList()  
# list2.insertEnd(Node(2))
# list2.insertEnd(Node(3))
# list2.insertEnd(Node(10))
# list2.insertEnd(Node(12))
# list2.insertEnd(Node(119))
# head2=list2.insertEnd(Node(60))
# printList(head2)

# head3=merge(head1,head2)
# printList(head3)