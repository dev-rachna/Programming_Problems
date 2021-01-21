'''
leetcode 230. Kth Smallest Element in a BST
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self, node):
        self.root = node


def insert(root, node):
    if root is None:
        root = node
        return
    if root.val < node.val:
        if root.right is None:
            root.right = node
        else:
            insert(root.right, node)

    else:
        if root.left is None:
            root.left = node
        else:
            insert(root.left, node)

def inorder(root, k):
    
    if root is None:
        return 0
    
    inorder(root.left,k)
    k[0]-=1
    if k[0]==0:
        print(root.val)
        return root.val
    inorder(root.right,k)




def kthSmallest(root, k):

    if root is None:
        return 0
    print(k, root.val)
    left = kthSmallest(root.left, k)
    print('l', left)
    if left:
        return left

    k[0] -= 1
    print('k', k, root.val)
    if k[0] == 0:
        return root.val

    right = kthSmallest(root.right, k)
    print('r', right)
    return right


bst = BST(Node(5))
insert(bst.root, Node(7))
insert(bst.root, Node(3))
insert(bst.root, Node(4))
insert(bst.root, Node(6))
insert(bst.root, Node(8))

print(kthSmallest(bst.root, [3]))
print(inorder(bst.root,[1]))
