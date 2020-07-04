# -*- coding: utf-8 -*-

class TreeNode():  
  
    def __init__(self, data):  
        self.key = data 
        self.left = None
        self.right = None



def swap(root):
    if root is None:
        return root
    
    swap(root.left)
    swap(root.right)
    
    root.right,root.left=root.left,root.right
    return root

def invertTree(root):
    root=swap(root)
    return root
 
def inorder(temp):   
    if (not temp): 
        return  
    inorder(temp.left)  
    print(temp.key,end = " ") 
    inorder(temp.right)
        
def insert(root,key): 
    temp=root
    q = []  
    q.append(temp)  
  
    # Do level order traversal until we find  
    # an empty place.  
    while (len(q)):  
        temp = q[0]  
        q.pop(0)  
  
        if (not temp.left): 
            temp.left = TreeNode(key)  
            break
        else: 
            q.append(temp.left)  
  
        if (not temp.right): 
            temp.right = TreeNode(key)  
            break
        else: 
            q.append(temp.right)
            
root = TreeNode(10)  
root.left = TreeNode(11)  
root.left.left = TreeNode(7)  
root.right = TreeNode(9)  
root.right.left = TreeNode(15)  
root.right.right = TreeNode(8) 
print("Inorder traversal before insertion:", end = " ") 
inorder(root)  
  
key = 12
insert(root, key)  
  
print()  
print("Inorder traversal after insertion:", end = " ") 
# inorder(root) 

root_inv=invertTree(root)
inorder(root_inv)

