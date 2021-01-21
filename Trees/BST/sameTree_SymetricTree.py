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
leetcode 100. Same Tree
'''

        
def sameTree(root1,root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None and root1.val==root2.val:
        return sameTree(root1.left,root2.left) and sameTree(root1.right,root2.right)
    else:
        return False


def symetricTree(root1,root2):
    if root1 is None and root2 is None:
        return True
    elif root1 is not None and root2 is not None and root1.val==root2.val:
        return symetricTree(root1.left,root2.right) and symetricTree(root1.right,root2.left)
    else:
        return False
    

bst=BST(Node(5))
insert(bst.root,Node(7))
insert(bst.root,Node(3))
insert(bst.root,Node(4))
insert(bst.root,Node(6))
insert(bst.root,Node(8))

bst2=BST(Node(5))
insert(bst2.root,Node(7))
insert(bst2.root,Node(3))
insert(bst2.root,Node(4))
insert(bst2.root,Node(6))
insert(bst2.root,Node(8))


print(sameTree(bst.root,bst2.root))