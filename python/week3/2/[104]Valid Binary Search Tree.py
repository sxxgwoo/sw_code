'''
Valid Binary Search Tree
Given the root of a binary tree, return true if it is a valid binary search tree, otherwise return false.

A valid binary search tree satisfies the following constraints:

The left subtree of every node contains only nodes with keys less than the node's key.
The right subtree of every node contains only nodes with keys greater than the node's key.
Both the left and right subtrees are also binary search trees.
Example 1:



Input: root = [2,1,3]

Output: true
Example 2:



Input: root = [1,2,3]

Output: false
Explanation: The root node's value is 1 but its left child's value is 2 which is greater than 1.
'''
class Queue:
    def __init__(self):
        self.data = []

    def append(self, val):
        self.data.append(val)

    def popleft(self):
        if self.data:
            return self.data.pop(0)
        raise IndexError("pop from empty queue")

    def __len__(self):
        return len(self.data)

    def __bool__(self):
        return bool(self.data)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(
                node.right, node.val, right
            )

        return valid(root, float("-inf"), float("inf"))
    
# 입력 리스트를 TreeNode로 변환하는 유틸리티 함수
def build_tree(nodes):
    if not nodes or nodes[0] is None:
        return None
    root = TreeNode(nodes[0])
    q = Queue()
    q.append(root)
    i = 1
    while i < len(nodes):
        node = q.popleft()
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            q.append(node.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            q.append(node.right)
        i += 1
    return root
if __name__=="__main__":
    sol = Solution()

    # Example 1
    root1 = build_tree([5,4,6,None,None,3,7])
    print(sol.isValidBST(root1)) 

    # Example 2
    root2 = build_tree([1, 2, 3])
    print(sol.isValidBST(root2)) 
