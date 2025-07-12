# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Problem description
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Solution 1: Dummy Node + Head-Insertion
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    """
    1-based 인덱스 left에서 right까지 구간을 한 번에 뒤집는 방법.
    더미 헤드를 써서 경계 처리를 깔끔히 합니다.
    시간 복잡도: O(n), 공간 복잡도: O(1)
    """
    if not head or left == right:
        return head

    # 1) 더미 노드를 만들어 head 앞에 연결
    dummy = ListNode(0)
    dummy.next = head

    # 2) reverse 구간 바로 앞(left-1) 노드를 prev에 위치시킴
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next  # left 직전 노드로 이동

    # 3) curr은 실제 뒤집기 시작 위치(= left 위치)
    curr = prev.next

    # 4) [left..right] 구간을 head-insertion 방식으로 뒤집기
    #    예: 1->2->3->4->5, left=2, right=4 일 때
    #    prev:1, curr:2
    #    반복문 한번 돌면 1->3->2->4->5, curr은 여전히 2
    for _ in range(right - left):
        nxt = curr.next           # 뒤집을 노드 (구간 내 두 번째)
        curr.next = nxt.next      # curr 다음을 건너뛰어 연결
        nxt.next = prev.next      # nxt를 reverse 구간 맨 앞에 삽입
        prev.next = nxt           # prev가 nxt를 가리키도록

    # 5) 더미의 다음이 새 헤드
    return dummy.next

# Example usage
def build_list(arr: list[int]) -> Optional[ListNode]:
    """파이썬 리스트 → 연결 리스트"""
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def to_list(head: Optional[ListNode]) -> list[int]:
    """연결 리스트 → 파이썬 리스트"""
    arr = []
    cur = head
    while cur:
        arr.append(cur.val)
        cur = cur.next
    return arr

# ─────────────────────────────────
# 테스트 케이스 (입력 리스트, left, right, 기대 출력 리스트)
test_cases = [
    # 문제 예제 1
    ([1,2,3,4,5], 1, 3, [3,2,1,4,5]),
    # 문제 예제 2 (left==right)
    ([1,1],     1, 1, [1,1]),
    # 추가 1: 뒤쪽 구간만 뒤집기
    ([1,2,3,4], 2, 4, [1,4,3,2]),
    # 추가 2: 앞쪽 구간만 뒤집기
    ([5,6,7,8], 1, 2, [6,5,7,8]),
    # 추가 3: 전체 뒤집기
    ([9,10,11], 1, 3, [11,10,9]),
    # 추가 4: 길이 1 리스트
    ([42],      1, 1, [42]),
    # 추가 5: 중간 한 원소만 (left=right)
    ([1,2,3],   2, 2, [1,2,3]),
]

if __name__ == "__main__":
    for i, (inp, left, right, expected) in enumerate(test_cases, 1):
        head = build_list(inp)
        out_head = reverseBetween(head, left, right)
        result = to_list(out_head)
        assert result == expected, (
            f"테스트 {i} 실패:\n"
            f"  입력 = {inp}, left={left}, right={right}\n"
            f"  출력 = {result}\n"
            f"  기대 = {expected}"
        )
        print(f"테스트 {i} 통과: {result}")