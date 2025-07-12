# 141. Linked List Cycle    
# https://leetcode.com/problems/linked-list-cycle/
# Problem description
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Solution 1: Floyd's Tortoise and Hare Algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    """
    플로이드의 토끼와 거북이 알고리즘을 사용한 사이클 검출
    시간 복잡도: O(n), 공간 복잡도: O(1)
    """
    slow = head  # 한 칸씩 이동
    fast = head  # 두 칸씩 이동

    # fast와 fast.next가 유효할 때까지 반복
    while fast and fast.next:
        slow = slow.next          # 거북이 한 칸
        fast = fast.next.next     # 토끼 두 칸
        
        # 두 포인터가 만나면 사이클 존재
        if slow is fast:
            return True

    # fast가 끝에 도달하면 사이클 없음
    return False

# Example usage
# 예시 1: 사이클이 없는 리스트
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
print(hasCycle(a))  # 출력: False

# 예시 2: 사이클이 있는 리스트
x = ListNode(1)
y = ListNode(2)
z = ListNode(3)
x.next = y
y.next = z
z.next = y  # y로 다시 연결 → 사이클
print(hasCycle(x))  # 출력: True