'''
Subtree of Another Tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:

Input: root = [1,2,3,4,5], subRoot = [2,4,5]

Output: true

Example 2:

Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]

Output: false
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Depth First Search
def sameTree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not root and not subRoot:
        return True
    if root and subRoot and root.val == subRoot.val:
        return (sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right))
    return False

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    if not subRoot:
        return True
    if not root:
        return False

    if sameTree(root, subRoot):
        return True
    return (isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot))

# Serialization And Pattern Matching
def serialize(root: TreeNode) -> str:
    if root == None:
        return "$#"

    return ("$" + str(root.val) + serialize(root.left) + serialize(root.right))  

def z_function(s: str) -> list:
    z = [0] * len(s)
    l, r, n = 0, 0, len(s)
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
    return z

def isSubtree(root: TreeNode, subRoot: TreeNode) -> bool:
    serialized_root = serialize(root)
    serialized_subRoot = serialize(subRoot)
    combined = serialized_subRoot + "|" + serialized_root

    z_values = z_function(combined)
    sub_len = len(serialized_subRoot)

    for i in range(sub_len + 1, len(combined)):
        if z_values[i] == sub_len:
            return True
    return False

# ============================
# Test Case [1,2,3,4,5,null,null,6], [2,4,5] -> false
# ============================
if __name__ == "__main__":
    root = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    node4 = TreeNode(5)
    node5 = TreeNode(6)

    subroot = TreeNode(2)
    subnode1 = TreeNode(4)
    subnode2 = TreeNode(5)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node3.left = node5

    subroot.left = subnode1
    subroot.right = subnode2
    
    res = isSubtree(root, subroot)

    print(res)