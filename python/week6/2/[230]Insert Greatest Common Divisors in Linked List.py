'''
Insert Greatest Common Divisors in Linked List
You are given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the head of the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Example 1:

Input: head = [12,3,4,6]

Output: [12,3,3,1,4,2,6]
Example 2:

Input: head = [2,1]

Output: [2,1,1]
'''
# 문제:
# 인접한 두 노드 (a, b) 사이에 gcd(a, b)를 값으로 갖는 새 노드를 삽입.
# 예) [12, 3, 4, 6] -> [12, 3, 3, 1, 4, 2, 6]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: ListNode) -> ListNode:
        # 유클리드 호제법 (반복)
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        cur = head
        # cur와 cur.next 쌍을 보며 순회
        while cur.next:
            n1, n2 = cur.val, cur.next.val
            # (n1, n2)의 gcd 값을 갖는 노드를 현재(cur)와 다음(cur.next) 사이에 삽입
            # 새 노드의 next는 기존 cur.next로, cur.next는 새 노드로 교체
            cur.next = ListNode(gcd(n1, n2), cur.next)
            # 다음 비교는 원래 다음 노드와 그 다음 노드의 쌍이므로 2칸 이동
            cur = cur.next.next

        return head


# ===== 테스트 유틸 =====
def build_linked_list(arr):
    """파이썬 리스트 -> 단일 연결 리스트"""
    if not arr:
        return None
    dummy = ListNode(0)
    tail = dummy
    for x in arr:
        tail.next = ListNode(x)
        tail = tail.next
    return dummy.next

def to_list(head):
    """단일 연결 리스트 -> 파이썬 리스트"""
    out = []
    cur = head
    while cur:
        out.append(cur.val)
        cur = cur.next
    return out


# ===== 예시 실행 =====
if __name__ == "__main__":
    sol = Solution()

    head1 = build_linked_list([12, 3, 4, 6])
    ans1 = sol.insertGreatestCommonDivisors(head1)
    print(to_list(ans1))  # [12, 3, 3, 1, 4, 2, 6]

    head2 = build_linked_list([2, 1])
    ans2 = sol.insertGreatestCommonDivisors(head2)
    print(to_list(ans2))  # [2, 1, 1]