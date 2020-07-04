# -*- coding: utf-8 -*-


class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    

class BST:
    def __init__(self,node):
        self.root=node

    
def insert(root,node):
    if root is None:
        root=node
        return
    if root.val<node.val:
        if root.right is None:
            root.right=node
        else:
            insert(root.right,node)
            
    else:
        if root.left is None:
            root.left=node
        else:
            insert(root.left,node)
            

'''
validate if given tress is BST
'''
def checkBST(root,mini,maxi):
    if root is None:
        return True
    elif root.val<maxi and root.val>mini and checkBST(root.left,mini,root.val) and checkBST(root.right,root.val,maxi):
        return True
    else:
        return False

#incomplete
def deleteNode(root,node):
    if root is None:
        return 
    elif root.val<node:
        deleteNode(root.right, node)
    elif root.val>node:
        deleteNode(root.left, node)
    else:
        if root.left is None and root.right is None:
            root=None
            # print(root.val)
            return
        elif root.left is None:
            root=root.right
            
            return 
        elif root.right is None:
            root=root.left
            
        else:
            temp=root.right
            while temp.left:
                temp=temp.left
            # print('t',temp.val)
            # # print(root.right.val)
            root.val=temp.val
            root.right=deleteNode(root.right,root.val)
        return root
            
def inorder(root):    
    if root is None:
        return    
    inorder(root.left)
    print(root.val)    
    inorder(root.right)              


bst=BST(Node(5))
insert(bst.root,Node(7))
insert(bst.root,Node(3))
insert(bst.root,Node(4))
insert(bst.root,Node(6))
insert(bst.root,Node(8))

print(checkBST(bst.root,-1*float('inf'),float('inf')))
inorder(bst.root)
deleteNode(bst.root,8)
print('------------')
inorder(bst.root)