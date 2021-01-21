# -*- coding: utf-8 -*-

'''
GFG
count leaf nodes in a binary tree
'''
import collections


class TreeNode():

    def __init__(self, data):
        self.key = data
        self.left = None
        self.right = None


def inorder(temp):
    if (not temp):
        return
    inorder(temp.left)
    print(temp.key, end=" ")
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


# def countLeaf(root):
#     if root is None:
#         return 0

#     if root.left is None and root.right is None:
#         return 1

#     else:
#         return countLeaf(root.left)+countLeaf(root.right)

ans=[0]
def countl(root,ans):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        ans[0]+=1
    else:
        countl(root.left,ans)
        countl(root.right,ans)


def countLeafIter(root):
    if root is None:
        return 0
    count = 0
    que = collections.deque()
    que.append(root)
    while que:
        temp = que.popleft()

        if temp.left is not None:
            que.append(temp.left)
        if temp.right is not None:
            que.append(temp.right)
        if temp.left is None and temp.right is None:

            count += 1
        # print(que[-1])
    return count


root = TreeNode(10)

arr = [15, 20, 1, 2, 3, 6, 7, 90]
for i in arr:
    insert(root, i)

# inorder(root)
# print(countLeaf(root))
countl(root,ans)
print(ans[0])
# print(countLeafIter(root))
