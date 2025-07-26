'''
House Robber III
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

In this new place, there are houses and each house has its only one parent house. All houses in this place form a binary tree. 
It will automatically contact the police if two directly-linked houses were broken.

You are given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Example 1:



Input: root = [1,4,null,2,3,3]

Output: 7
Explanation: Maximum amount of money the thief can rob = 4 + 3 = 7

Example 2:



Input: root = [1,null,2,3,5,4,2]

Output: 12
Explanation: Maximum amount of money the thief can rob = 1 + 4 + 2 + 5 = 12
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

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1) Recursion -> 느림
    # def rob(self, root: TreeNode) -> int:
    #     if not root:
    #         return 0
    #     res = root.val
    #     if root.left:
    #         res += self.rob(root.left.left) + self.rob(root.left.right)
    #     if root.right:
    #         res += self.rob(root.right.left) + self.rob(root.right.right)
        
    #     res = max(res, self.rob(root.left) + self.rob(root.right))
        
    #     return res
    # 2) Dynamic Programming (Optimal)

    def rob(self, root: TreeNode) -> int:
        # DFS를 통해 각 노드에서 두 가지 경우의 최대 이익을 계산:
        # [0] 현재 노드를 도둑질할 경우의 최대 이익
        # [1] 현재 노드를 도둑질하지 않을 경우의 최대 이익
        def dfs(root):
            if not root:
                # 노드가 없으면 두 경우 모두 이익은 0
                return [0, 0]

            # 왼쪽, 오른쪽 서브트리의 결과를 재귀적으로 계산
            leftPair = dfs(root.left)
            rightPair = dfs(root.right)

            # 현재 노드를 도둑질할 경우: 자식 노드는 도둑질 못함
            withRoot = root.val + leftPair[1] + rightPair[1]

            # 현재 노드를 도둑질하지 않을 경우: 자식 노드는 도둑질 할 수도, 안 할 수도 있음 (최대값 선택)
            withoutRoot = max(leftPair) + max(rightPair)

            # 현재 노드에서 [도둑질하는 경우, 도둑질하지 않는 경우] 리턴
            return [withRoot, withoutRoot]

        # 루트 노드에서 도둑질 하거나 하지 않았을 때의 최대 이익 중 더 큰 값 리턴
        return max(dfs(root))

if __name__=="__main__":
    sol = Solution()

    root1 = build_tree([1,4,None,2,3,3])
    print(sol.rob(root1))