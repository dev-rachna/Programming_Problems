'''
leetcode 328. Odd Even Linked List
Given a singly linked list, group all odd nodes together followed by the even nodes
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertEnd(self, node):
        if self.head is None:
            self.head = node

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        node.next = None


def oddEvenList(head):
    if head is None:
        return head

    odd = head
    even = head.next
    even_head = even

    curr = head

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next

    odd.next = even_head
    return curr


def printList(head):
    if head is None:
        print('empty list')
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


list1 = LinkedList()
list1.insertEnd(Node(1))
list1.insertEnd(Node(2))
list1.insertEnd(Node(3))
list1.insertEnd(Node(4))
list1.insertEnd(Node(5))
list1.insertEnd(Node(6))

# printList(list1.head)

head1 = oddEvenList(list1.head)
printList(head1)
