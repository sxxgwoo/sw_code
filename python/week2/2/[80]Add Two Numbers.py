'''
Add Two Numbers
You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Example 1:



Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.
Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()  # 결과 리스트의 시작을 위한 더미 노드 생성
        cur = dummy         # 결과 리스트를 구성해 나갈 포인터

        carry = 0           # 자리 올림(carry)을 저장할 변수
        while l1 or l2 or carry:
            # 각 노드의 값이 존재하면 가져오고, 없으면 0으로 처리
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # 새로운 자리수 계산
            val = v1 + v2 + carry     # 현재 자리 합계
            carry = val // 10         # 10 이상이면 자리 올림 발생
            val = val % 10            # 현재 자리에 들어갈 숫자 (0~9)

            # 결과 리스트에 현재 자릿수 노드 추가
            cur.next = ListNode(val)

            # 포인터 이동
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next

if __name__ == "__main__":
    # 입력 리스트: [1, 2, 3]과 [4, 5, 6]
    l1_vals = [1, 2, 3]
    l2_vals = [4, 5, 6]

    # 연결 리스트로 변환
    def build_linked_list(values):
        dummy = ListNode()
        cur = dummy
        for val in values:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next

    l1 = build_linked_list(l1_vals)
    l2 = build_linked_list(l2_vals)

    # 계산
    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    # 결과 출력
    output = []
    while result:
        output.append(result.val)
        result = result.next
    print(output)  # 예상 출력: [5, 7, 9]
