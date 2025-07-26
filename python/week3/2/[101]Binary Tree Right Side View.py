'''
Binary Tree Right Side View
You are given the root of a binary tree. Return only the values of the nodes that are visible from the right side of the tree, ordered from top to bottom.

Example 1:



Input: root = [1,2,3]

Output: [1,3]
Example 2:



Input: root = [1,2,3,4,5,6,7]

Output: [1,3,7]
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
    # 1) DFS
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []

        def dfs(node, depth):
            if not node:
                return None
            if depth == len(res):   # key point임
                res.append(node.val)
            
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return res
    
    # 2) BFS
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        q = Queue()
        q.append(root)

        while q:
            rightSide = None
            qLen = len(q)

            for i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res

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

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    root1 = build_tree([1, 2, 3])
    print("Output:", sol.rightSideView(root1))  # Output: [1, 3]

    # Example 2
    root2 = build_tree([1, 2, 3, 4, 5, 6, 7])
    print("Output:", sol.rightSideView(root2))  # Output: [1, 3, 7]

    