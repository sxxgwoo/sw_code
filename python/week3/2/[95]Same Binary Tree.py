'''
Same Binary Tree
Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.

Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

Example 1:



Input: p = [1,2,3], q = [1,2,3]

Output: true
Example 2:



Input: p = [4,7], q = [4,null,7]

Output: false
Example 3:



Input: p = [1,2,3], q = [1,3,2]

Output: false
'''
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 1) DFS
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
    # 2) BFS
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                nodeP = q1.popleft()
                nodeQ = q2.popleft()

                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False

                q1.append(nodeP.left)
                q1.append(nodeP.right)
                q2.append(nodeQ.left)
                q2.append(nodeQ.right)

        return True

# 리스트를 트리로 변환하는 함수
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if i < len(nodes) and nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root

if __name__ == "__main__":
    sol = Solution()

    # Example 1: 같은 구조와 값
    tree1 = build_tree([1, 2, 3])
    tree2 = build_tree([1, 2, 3])
    print("Example 1:", sol.isSameTree(tree1, tree2))  # True

    # Example 2: 다른 구조
    tree3 = build_tree([1, 2])
    tree4 = build_tree([1, None, 2])
    print("Example 2:", sol.isSameTree(tree3, tree4))  # False

    # Example 3: 같은 구조, 다른 값
    tree5 = build_tree([1, 2, 1])
    tree6 = build_tree([1, 1, 2])
    print("Example 3:", sol.isSameTree(tree5, tree6))  # False

    