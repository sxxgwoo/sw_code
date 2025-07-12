# 94. Binary Tree Inorder Traversal
# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Problem description
# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Solution 1: Recursive Inorder Traversal
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import Optional, List

def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    재귀를 사용한 중위 순회
    """
    res = []
    _dfs(root, res)
    return res

def _dfs(node: Optional[TreeNode], res: List[int]):
    if not node:
        return
    # 1) 왼쪽 서브트리 순회
    _dfs(node.left, res)
    # 2) 현재 노드 방문
    res.append(node.val)
    # 3) 오른쪽 서브트리 순회
    _dfs(node.right, res)
    
# Solution 2: Iterative Inorder Traversal
# Time Complexity: O(n)
# Space Complexity: O(n)

# def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
#     """
#     스택을 사용한 중위 순회 (반복)
#     """
#     res, stack = [], []
#     curr = root

#     # curr이 None이 될 때까지 또는 스택이 빌 때까지 반복
#     while curr or stack:
#         # 왼쪽 끝까지 계속 스택에 쌓기
#         while curr:
#             stack.append(curr)
#             curr = curr.left

#         # 더 이상 왼쪽이 없으면 스택에서 꺼내 방문
#         curr = stack.pop()
#         res.append(curr.val)

#         # 오른쪽 서브트리로 이동
#         curr = curr.right

#     return res

# Test cases
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(inorderTraversal(root))  # [1, 3, 2]