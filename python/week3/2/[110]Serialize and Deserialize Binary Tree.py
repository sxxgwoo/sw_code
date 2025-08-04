'''
Serialize and Deserialize Binary Tree
Implement an algorithm to serialize and deserialize a binary tree.

Serialization is the process of converting an in-memory structure into a sequence of bits so that it can be stored or sent across a network to be reconstructed later in another computer environment.

You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure. There is no additional restriction on how your serialization/deserialization algorithm should work.

Note: The input/output format in the examples is the same as how NeetCode serializes a binary tree. You do not necessarily need to follow this format.

Example 1:



Input: root = [1,2,3,null,null,4,5]

Output: [1,2,3,null,null,4,5]
Example 2:

Input: root = []

Output: []
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

# Codec 클래스: 이진 트리의 직렬화/역직렬화를 담당
class Codec:
    """
    Codec 클래스는 이진 트리를 문자열로 직렬화하고,
    문자열로부터 원래의 트리 구조를 복원하는 기능을 제공한다.

    직렬화 방식: DFS 전위 순회 (preorder traversal)
    - 노드 값은 쉼표로 구분된 문자열로 저장
    - None(null) 노드는 "N"으로 표시
    """

    def serialize(self, root: TreeNode) -> str:
        """
        이진 트리를 문자열로 직렬화한다.
        - 전위 순회를 사용하여 왼쪽 → 오른쪽 순서로 탐색
        - 노드가 없으면 "N"을 기록한다.
        """
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))  # 현재 노드 값 기록
            dfs(node.left)             # 왼쪽 서브트리 탐색
            dfs(node.right)            # 오른쪽 서브트리 탐색

        dfs(root)
        return ",".join(res)

    def deserialize(self, data: str) -> TreeNode:
        """
        직렬화된 문자열을 기반으로 이진 트리를 복원한다.
        - 문자열을 쉼표로 나누어 리스트로 만든 후
        - 전위 순회 순서대로 재귀적으로 트리를 구성
        """
        vals = data.split(",")
        self.i = 0  # 현재 탐색 중인 인덱스

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))  # 노드 생성
            self.i += 1
            node.left = dfs()   # 왼쪽 자식 설정
            node.right = dfs()  # 오른쪽 자식 설정
            return node

        return dfs()

# 실행 코드
if __name__ == "__main__":
    # 예제 트리: [1,2,3,None,None,4,5]
    input_list = [1, 2, 3, None, None, 4, 5]
    root = build_tree(input_list)

    codec = Codec()
    serialized = codec.serialize(root)
    print("Serialized:", serialized)

    deserialized_root = codec.deserialize(serialized)
    re_serialized = codec.serialize(deserialized_root)
    print("Re-Serialized:", re_serialized)
    