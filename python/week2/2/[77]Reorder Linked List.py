'''
Reorder Linked List
You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:

Input: head = [2,4,6,8]

Output: [2,8,4,6]
Example 2:

Input: head = [2,4,6,8,10]

Output: [2,10,4,8,6]
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    #1) Brute Force
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        
        i, j = 0, len(nodes) - 1
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        
        nodes[i].next = None
    # 2) Recursion
    def reorderList(self, head: ListNode) -> None:

        def rec(root: ListNode, cur: ListNode) -> ListNode:
            # base case: cur가 None이면 재귀 종료, root 반환 (root는 head에서 시작)
            if not cur:
                return root

            # 재귀적으로 끝까지 들어감 (cur는 끝 노드로 이동)
            root = rec(root, cur.next)
            
            # root가 None이면, 더 이상 연결할 노드 없음
            if not root:
                return None

            tmp = None  # root의 다음 노드를 저장할 임시 변수

            # root와 cur가 같거나 서로 인접한 경우 (중간에서 만나거나 바로 연결됨)
            if root == cur or root.next == cur:
                cur.next = None  # 리스트의 중간 지점을 만난 경우 연결 끊고 종료
            else:
                tmp = root.next  # 현재 root의 다음 노드를 저장
                root.next = cur  # root 다음에 현재 cur을 연결
                cur.next = tmp   # cur 다음에 원래 root 다음 노드를 연결

            # 다음 루프에 사용할 새로운 root 위치를 반환
            return tmp

        # 재귀 호출 시작: root는 head, cur은 head의 다음 노드
        head = rec(head, head.next)


# 연결 리스트를 프린트하는 함수
def printList(head: ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    print(result)

if __name__ == "__main__":
    sol = Solution()
    input = [2, 4, 6, 8, 10]

    # Step 0: 배열을 연결 리스트로 변환
    dummy = ListNode(0)
    curr = dummy
    for val in input:
        curr.next = ListNode(val)
        curr = curr.next

    # dummy 다음을 head로 해서 out
    head = dummy.next

    # reorderList 실행
    sol.reorderList(head)

    # 결과 출력
    printList(head)