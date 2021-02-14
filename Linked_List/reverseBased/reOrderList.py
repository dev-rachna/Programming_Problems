
def reverseFrom(head):
  if head is None:
    return "empty"
  prev=None
  curr=head
  next=None

  while curr.next:
    next=curr.next
    curr.next=prev
    prev=curr
    curr=next
  
  curr.next=prev
  head=curr
  return head
  


#start
def middle(head):
  if head is None:
    return "empty"
  
  curr=head
  slow=head
  fast=head
  while fast.next and fast.next.next:
    slow=slow.next
    fast=fast.next.next
  
  l2=reverseFrom(slow.next)
  slow.next=None
  merge(curr,l2)
  



def merge(l1,l2):
  if l1 is None:
    return "empty"
  head=l1

  while l2:
    next1=l1.next
    l1.next=l2
    l1=l2
    l2=next1
  return head

