'''
Kth Smallest Integer in BST

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) in the tree.

A binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.

Example 1:

Input: root = [2,1,3], k = 1

Output: 1

Example 2:

Input: root = [4,3,5,2,null], k = 4

Output: 5
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Inorder Traversal
def kthSmallest(root: TreeNode, k: int) -> int:
    arr = []

    def dfs(node):
        if not node:
            return
        
        dfs(node.left)
        arr.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return arr[k - 1]

# Brute Force
def merge(lst1, lst2):
    i=j=0
    res = []

    while i < len(lst1) and j < len(lst2):
        if(lst1[i] > lst2[j]):
            res.append(lst2[j])
            j += 1
        else:
            res.append(lst1[i])
            i += 1
        
    if(i == len(lst1)):
        res.extend(lst2[j:])
    if(j == len(lst2)):
        res.extend(lst1[i:])
    
    return res

def mergeSort(lst):
    if(len(lst) <= 1):
        return lst
    mid = len(lst) // 2

    lst1 = mergeSort(lst[:mid])
    lst2 = mergeSort(lst[mid:])

    return merge(lst1, lst2)

def kthSmallest(root: TreeNode, k: int) -> int:
    arr = []

    def dfs(node):
        if not node:
            return
        
        arr.append(node.val)
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)
    arr.sort()
    return arr[k - 1]

# ============================
# Test Case [4,3,5,2,null], 4 -> 5
# ============================
if __name__ == "__main__":
    root = TreeNode(4)
    node1 = TreeNode(3)
    node2 = TreeNode(5)
    node3 = TreeNode(2)

    root.left = node1
    root.right = node2
    node1.left = node3
    
    res = kthSmallest(root, 4)

    print(res)