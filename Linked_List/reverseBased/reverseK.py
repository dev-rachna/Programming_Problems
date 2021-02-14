
def reverse(tail,k):
  curr=tail
  prev=None
  next1=None
  while curr:
    next1=curr.next
    curr.next=prev
    prev=curr
    curr=next1
  head=prev
  return head


def reverseSpecific(head,k):
  if head is None:
    return "empty"
  
  res=node(0)
  res.next=head
  prev=res
  curr=head
  
  ind=0
  while curr:
    ind=0
    tail=curr
    for _ in range(k+1):
      if curr:
        curr=curr.next
        ind+=1
      else:
        break

    if ind!=k:
      prev.next=tail
    else:
      prev.next=reverse(tail,k)
      prev=tail
    
  
  return res.next
