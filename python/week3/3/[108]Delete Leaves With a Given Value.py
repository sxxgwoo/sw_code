'''
Delete Leaves With a Given Value

You are given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

Example 1:

Input: root = [1,2,3,5,2,2,5], target = 2

Output: [1,2,3,5,null,null,5]

Example 2:

Input: root = [3,null,3,3], target = 3

Output: []

Explanation: The output is an empty tree after removing all the nodes with value 3.
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursion (Postorder Traversal)
def removeLeafNodes(root: TreeNode, target: int) -> TreeNode:
    if not root:
        return None

    root.left = removeLeafNodes(root.left, target)
    root.right = removeLeafNodes(root.right, target)

    if not root.left and not root.right and root.val == target:
        return None

    return root

# Iterative Postorder Traversal
def removeLeafNodes(root: TreeNode, target: int) -> TreeNode:
    stack = [root]
    visit = set()
    parents = {root: None}

    while stack:
        node = stack.pop()
        if not node.left and not node.right:
            if node.val == target:
                p = parents[node]
                if not p:
                    return None
                if p.left == node:
                    p.left = None
                if p.right == node:
                    p.right = None
        elif node not in visit:
            visit.add(node)
            stack.append(node)
            if node.left:
                stack.append(node.left)
                parents[node.left] = node
            if node.right:
                stack.append(node.right)
                parents[node.right] = node

    return root

# ============================
# Test Case [1,2,3,5,2,2,5], 2 -> [1,2,3,5,null,null,5]
# ============================
if __name__ == "__main__":
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(5)
    node4 = TreeNode(2)
    node5 = TreeNode(2)
    node6 = TreeNode(5)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    node2.right = node6
    
    res = removeLeafNodes(root, 2)

    def DFS(root):
        if(root):
            print(root.val)
            DFS(root.left)
            DFS(root.right)

    DFS(res)