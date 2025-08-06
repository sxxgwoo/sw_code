'''
Diameter of Binary Tree

The diameter of a binary tree is defined as the length of the longest path between any two nodes within the tree. The path does not necessarily have to pass through the root.

The length of a path between two nodes in a binary tree is the number of edges between the nodes.

Given the root of a binary tree root, return the diameter of the tree.

Example 1:

Input: root = [1,null,2,3,4,5]

Output: 3

Explanation: 3 is the length of the path [1,2,3,5] or [5,3,2,4].

Example 2:

Input: root = [1,2,3]

Output: 2
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Brute Force
def diameterOfBinaryTree(root: TreeNode) -> int:
    if not root:
        return 0
    
    leftHeight = maxHeight(root.left)
    rightHeight = maxHeight(root.right)
    diameter = leftHeight + rightHeight 
    sub = max(diameterOfBinaryTree(root.left), diameterOfBinaryTree(root.right))
    return max(diameter, sub)

def maxHeight(root: TreeNode) -> int:
    if not root:
        return 0

    return 1 + max(maxHeight(root.left), maxHeight(root.right))

# Depth First Search
def diameterOfBinaryTree(root: TreeNode) -> int:
    res = 0

    def dfs(root):
        nonlocal res

        if not root:
            return 0
        
        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right)

        return 1 + max(left, right)

    dfs(root)
    return res

# ============================
# Test Case [1,null,2,3,4,5] -> 3
# ============================
if __name__ == "__main__":
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)

    root.right = node1
    node1.left = node2
    node1.right = node3
    node2.left = node4
    
    res = diameterOfBinaryTree(root)

    print(res)