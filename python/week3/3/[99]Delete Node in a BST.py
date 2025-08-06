'''
Delete Node in a BST

You are given a root node reference of a BST and a key, delete the node with the given key in the BST, if present. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: There can be multiple results after deleting the node, return any one of them.

Example 1:

Input: root = [5,3,9,1,4], key = 3

Output: [5,4,9,1]

Explanation: Another valid answer is:

Example 2:

Input: root = [5,3,6,null,4,null,10,null,null,7], key = 3

Output: [5,4,6,null,null,null,10,7]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion 1
def deleteNode(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return root

    if key > root.val:
        root.right = deleteNode(root.right, key)
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        cur = root.right
        while cur.left:
            cur = cur.left
        root.val = cur.val
        root.right = deleteNode(root.right, root.val)

    return root

# Recursion 2
def deleteNode(root: TreeNode, key: int) -> TreeNode:
    if not root:
        return root

    if key > root.val:
        root.right = deleteNode(root.right, key)
    elif key < root.val:
        root.left = deleteNode(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        cur = root.right
        while cur.left:
            cur = cur.left
        cur.left = root.left
        res = root.right
        del root
        return res

    return root

# ============================
# Test Case [5,3,9,1,4], 3 -> [5,4,9,1]
# ============================
if __name__ == "__main__":
    root = TreeNode(5)
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(1)
    node4 = TreeNode(4)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    
    res = deleteNode(root, 3)

    def DFS(root):
        if(root):
            print(root.val)
            DFS(root.left)
            DFS(root.right)

    DFS(res)
