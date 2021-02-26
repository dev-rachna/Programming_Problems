def reverse(head):
    curr=head
    prev=None
    next1=None
    while curr:
        next1=curr.next
        curr.next=prev
        prev=curr
        curr=next1

    return next1



def fun(head):
    slow=head
    fast=head
    curr=fast
    while fast and fast.next:
        slow=slow.next
        fast=fast.next

    start=reverse(slow)

    while start:
        if curr.val!=start.val:
            return "Not plndrm"
        curr=curr.next 
        start=start.next
    
    return "Pallindrom"