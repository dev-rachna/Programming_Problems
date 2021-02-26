def reverse(head):
    if head is None:
        return "empty"
    curr=head
    prev=None
    next1=None

    while curr:
        next1=curr.next
        curr.next=prev
        prev=curr
        curr=next1
    
    return prev


def mergeList(l1,l2):
    curr=l1
    while l2:
        next1=l1.next
      
        l1.next=l2
        l1=l2
        l2=next1
    return curr

def fun(head):
    if head is None:
        return "empty"
    curr=head
    # find mid
    slow=head
    fast=head

    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    middle=slow.next
    slow.next=None
    # reverse from mid
    l2=reverse(middle)
    l1=curr

    return mergeList(l1,l2)

