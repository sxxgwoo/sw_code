'''
Binary Tree Preorder Traversal
You are given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:



Input: root = [1,2,3,4,5,6,7]

Output: [1,2,4,5,3,6,7]
Example 2:



Input: root = [1,2,3,null,4,5,null]

Output: [1,2,4,3,5]
Example 3:

Input: root = []

Output: []
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:

    # sw solution
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        if not root:
            return res
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        return res

# 리스트를 이진트리(TreeNode)로 변환하는 함수 (레벨 순서 기반)
def build_tree_from_list(vals):
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    sol = Solution()

    # 예시 입력
    input_list = [1, 2, 3, None, 4, 5, None]

    # 이진 트리로 변환
    root = build_tree_from_list(input_list)

    # 전위 순회 실행 및 출력
    output = sol.preorderTraversal(root)
    print(output)
