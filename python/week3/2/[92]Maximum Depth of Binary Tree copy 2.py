'''
#Binary Tree, DFS, BFS
Maximum Depth of Binary Tree
Given the root of a binary tree, return its depth.

The depth of a binary tree is defined as the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:



Input: root = [1,2,3,null,null,4]

Output: 3
Example 2:

Input: root = []

Output: 0
'''
# from collections import deque

# deque구현 간단한 Queue 클래스 구현 (FIFO)
class Queue:
    def __init__(self):
        self.data = []

    def append(self, val):
        self.data.append(val)

    def popleft(self):
        if self.data:
            return self.data.pop(0)  # O(n) 시간복잡도
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
    # 1) Recursive DFS
    # def maxDepth(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # 2) BFS
    def maxDepth(self, root: TreeNode) -> int:
        # q = deque()
        q=Queue()
        if root:
            q.append(root)  # 루트 노드가 존재하면 큐에 추가

        level = 0  # 트리의 깊이를 저장할 변수

        # 큐가 비어있지 않은 동안 반복
        while q:
            # 현재 레벨에 있는 노드 수 만큼 반복
            for _ in range(len(q)):
                node = q.popleft()  # 현재 노드를 큐에서 꺼냄

                # 왼쪽 자식이 있다면 큐에 추가
                if node.left:
                    q.append(node.left)
                # 오른쪽 자식이 있다면 큐에 추가
                if node.right:
                    q.append(node.right)

            # 현재 레벨의 모든 노드를 처리했으므로 깊이 1 증가
            level += 1

        # 모든 레벨을 순회한 후의 깊이를 반환
        return level

# 트리를 리스트로부터 생성하는 함수 (예: [1,2,3,None,None,4])
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    # q = deque([root])
    q = Queue()
    q.append(root)
    i = 1
    while q and i < len(nodes):
        node = q.popleft()
        if nodes[i] is not None:
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
    root1 = build_tree([1, 2, 3, None, None, 4])
    print("Output for Example 1:", sol.maxDepth(root1))  # Expected: 3

    # Example 2
    root2 = build_tree([])
    print("Output for Example 2:", sol.maxDepth(root2))  # Expected: 0
