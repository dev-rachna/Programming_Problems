# -*- coding: utf-8 -*-
import collections
class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class BST:
    def __init__(self,root):
        self.root=root
    

def insert(root,node):
    if root is None:
        root=node
        # print(root.val)
        return 
    if root.val<node.val:
        if root.right is None:
            root.right=node
        else:
            insert(root.right,node)
    elif root.val>node.val:
        if root.left is None:
            root.left=node
        else:
            insert(root.left,node)

def inorder(root):    
    if root is None:
        return    
    inorder(root.left)
    print(root.val)    
    inorder(root.right)
    

def preOrder(root):
    if root is None:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def postOrder(root):
    if root is None:
        return
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)


def levelOrder(root):
    if root is None:
        return
    
    que=collections.deque()
    que.append(root)
    
    while que:
        node=que.popleft()
        print(node.val)
        if node.left is not None:
            que.append(node.left)
        if node.right is not None:
            que.append(node.right)




bst=BST(Node(5))
insert(bst.root,Node(6))
insert(bst.root,Node(3))
insert(bst.root,Node(4))
print('inorder')
inorder(bst.root)
print('preorder')
preOrder(bst.root)
print('postorder')
postOrder(bst.root)
print('levelOrder')
levelOrder(bst.root)