'''
GFG 
Given a Binary Tree, find the maximum(or minimum) element in it.
'''


class TreeNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.data, end=" ")
    inorder(temp.right)


def insert(root, key):
    temp = root
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


def maximum(root):
    if root is None:
        return float('-inf')
    res = root.data
    left_res = maximum(root.left)
    right_res = maximum(root.right)
    return max(res, left_res, right_res)


root = TreeNode(10)

arr = [15, 20, 1, 2, 3, 6, 7, 90]
for i in arr:
    insert(root, i)

print(maximum(root))
