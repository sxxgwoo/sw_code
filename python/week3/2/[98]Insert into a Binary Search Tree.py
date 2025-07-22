'''
Insert into a Binary Search Tree
You are given the root node of a binary search tree (BST) and a value val to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Note: There may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:



Input: root = [5,3,9,1,4], val = 6

Output: [5,3,9,1,4,6]
Example 2:

Input: root = [5,3,6,null,4,null,10,null,null,7], val = 9

Output: [5,3,6,null,4,null,10,null,null,7,null,null,9]
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # 1) sw Recursion
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)
        return root
    
    # 2) Iteration
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val)

        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left

# 리스트를 BST 트리로 만드는 함수 (BFS 방식)
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while i < len(nodes):
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

# 트리를 리스트 형태로 다시 변환하는 함수 (레벨 순서)
def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # 뒤쪽 None 제거 (불필요한 null 제거)
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    sol = Solution()

    # Example 1
    root1 = build_tree([5, 3, 9, 1, 4])
    val1 = 6
    updated1 = sol.insertIntoBST(root1, val1)
    print("Example 1 Output:", tree_to_list(updated1))  # [5, 3, 9, 1, 4, 6]

    # Example 2
    root2 = build_tree([5, 3, 6, None, 4, None, 10, None, None, 7])
    val2 = 9
    updated2 = sol.insertIntoBST(root2, val2)
    print("Example 2 Output:", tree_to_list(updated2))  # [5, 3, 6, None, 4, None, 10, None, None, 7, None, None, 9]
