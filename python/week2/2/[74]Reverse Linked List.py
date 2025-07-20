'''
Reverse Linked List
Given the beginning of a singly linked list head, reverse the list, and return the new beginning of the list.

Example 1:

Input: head = [0,1,2,3]

Output: [3,2,1,0]
Example 2:

Input: head = []

Output: []

Optional[ListNode] -> head는 ListNode일 수도 있고, None일 수도 있다.
'''    
# from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    # 1) Recursion
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None

        newHead = head
        if head.next:
            # 재귀적으로 끝까지 이동하여 newHead를 반환
            newHead = self.reverseList(head.next)
            # 다음 노드의 next를 현재 노드로 설정하여 뒤집기
            head.next.next = head
        # 현재 노드의 next를 끊어서 꼬리로 만듦
        head.next = None
        
        return newHead
    
    # 2) Iteration
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head  # prev: 이전 노드, curr: 현재 노드

        while curr:
            temp = curr.next     # 다음 노드 저장
            curr.next = prev     # 현재 노드의 next를 이전 노드로 변경 (뒤집기)
            prev = curr          # prev를 현재 노드로 업데이트
            curr = temp          # curr를 다음 노드로 이동
        return prev              # prev가 새 리스트의 시작점이 됨

if __name__ == "__main__":
    sol = Solution()

    # input = [0, 1, 2, 3]
    input = []

    dummy = ListNode(0)
    curr = dummy
    for val in input:
        curr.next = ListNode(val)
        curr = curr.next
    head = dummy.next

    reversed_head = sol.reverseList(head)

    output = []
    while reversed_head:
        output.append(reversed_head.val)
        reversed_head = reversed_head.next

    print("Input: head =", input)
    print("Output:", output)