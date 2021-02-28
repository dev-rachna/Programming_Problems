def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    def reverse(head, k):
        count = 0
        curr = head
        prev = None
        next1 = None
        while count < k:
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
            count += 1
        return prev

    dummy = ListNode(0)

    prev = dummy
    curr = head
    tail = head
    while curr:
        tail = curr
        count = 0
        while count < k:

            if curr:
                # print(count,'c',curr.val)
                curr = curr.next

            else:
                break
            count += 1
        # if curr:
        #     print(curr.val)
        if count == k:
            # print(tail.val,'tail')
            prev.next = reverse(tail, k)
            # print(prev.val)
            prev = tail
        else:
            prev.next = tail
    return dummy.next
