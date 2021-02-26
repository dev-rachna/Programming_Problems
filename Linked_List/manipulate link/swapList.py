# -*- coding: utf-8 -*-


def fun(head):
    if head is None or head.next is None:
        return "Cant do it"
    first = head
    sec = head.next

    dummy = Node(0)
    res = dummy
    dummy.next = first

    while first.next and first.next.next:
        first.next = sec.next
        sec.next = first
        dummy.next = sec

        dummy = first
        first = first.next
        sec = first.next.next

    return res.next
