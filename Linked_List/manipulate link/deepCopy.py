# refer leetcode sol

def fun(head):
  if head is None:
    return "empty"
  
  first_org=head

  curr=head
  while curr:
    next1=curr.next1
    copy=Node(curr.data)
    curr.next=copy
    copy.next=next1
    curr=next1
  
  curr=first_org

  while curr:
    curr.next.random=curr.random.next
    # change syntax
    curr=curr.next ?curr.next.next :curr.next
  
  curr=first_org
  copy=first_org.next
  res=copy

  while curr and curr.next:
    curr.next=curr.next.next
    copy.next=copy.next.next
    curr=curr.next
    copy=copy.next 
  return res

  

  

  


  
