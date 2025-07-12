'''
Remove Node From End of Linked List

You are given the beginning of a linked list head, and an integer n.

Remove the nth node from the end of the list and return the beginning of the list.

Example 1:

Input: head = [1,2,3,4], n = 2

Output: [1,2,4]

Example 2:

Input: head = [5], n = 1

Output: []

Example 3:

Input: head = [1,2], n = 2

Output: [2]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Brute Force
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next
    
    removeIndex = len(nodes) - n
    if removeIndex == 0:
        return head.next
    
    nodes[removeIndex - 1].next = nodes[removeIndex].next
    return head

# Iteration (Two Pass)
def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    N = 0
    cur = head
    while cur:
        N += 1
        cur = cur.next
    
    removeIndex = N - n
    if removeIndex == 0:
        return head.next
    
    cur = head
    for i in range(N - 1):
        if (i + 1) == removeIndex:
            cur.next = cur.next.next
            break
        cur = cur.next
    return head

# ============================
# Test Case [1,2,3,4], 2 -> [1,2,4]
# ============================
if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)

    a.next = b
    b.next = c
    c.next = d

    res = removeNthFromEnd(a, 2)

    while(res):
        print(res.val)

        res = res.next