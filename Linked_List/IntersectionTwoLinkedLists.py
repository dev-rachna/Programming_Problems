'''
leetcode 160. Intersection of Two Linked Lists
Write a program to find the node at which the intersection of two singly linked lists begins.
'''


def getIntersectionNode(headA, headB):
    currA = headA
    currB = headB
    m = 0
    n = 0

    while currA:
        m += 1
        currA = currA.next

    while currB:
        n += 1
        currB = currB.next
    currA=headA
    currB=headB
    if m > n:
        for _ in range(m-n):
            currA = currA.next
    elif n > m:
        for _ in range(n-m):
            currB = currB.next

    while currA != currB:
        currA = currA.next
        currB = currB.next

    print(currA.val)
