'''
Binary Tree Postorder Traversal

You are given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,2,3,4,5,6,7]

Output: [4,5,2,6,7,3,1]

Example 2:

Input: root = [1,2,3,null,4,5,null]

Output: [4,2,5,3,1]

Example 3:

Input: root = []

Output: []
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search
def postorderTraversal(root: TreeNode) -> List[int]:
    res = []

    def postorder(node):
        if not node:
            return
        
        postorder(node.left)
        postorder(node.right)
        res.append(node.val)
    
    postorder(root)
    return res

# Iterative Depth First Search
def postorderTraversal(root: TreeNode) -> List[int]:
    stack = [root]
    visit = [False]
    res = []

    while stack:
        cur, v = stack.pop(), visit.pop()
        if cur:
            if v:
                res.append(cur.val)
            else:
                stack.append(cur)
                visit.append(True)
                stack.append(cur.right)
                visit.append(False)
                stack.append(cur.left)
                visit.append(False)

    return res

# ============================
# Test Case [1,2,3,null,4,5,null] -> [4,2,5,3,1]
# ============================
if __name__ == "__main__":
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)

    a.left = b
    a.right = c
    b.right = d
    c.left = e
    
    res = postorderTraversal(a)

    print(res)