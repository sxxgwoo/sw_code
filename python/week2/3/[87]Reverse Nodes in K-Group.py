'''
Reverse Nodes in K-Group

You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:

Input: head = [1,2,3,4,5,6], k = 3

Output: [3,2,1,6,5,4]

Example 2:

Input: head = [1,2,3,4,5], k = 3

Output: [3,2,1,4,5]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursion
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    cur = head
    group = 0
    while cur and group < k:
        cur = cur.next
        group += 1

    if group == k:
        cur = reverseKGroup(cur, k)
        while group > 0:
            tmp = head.next
            head.next = cur
            cur = head
            head = tmp
            group -= 1
        head = cur
    return head

#Iteration
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0, head)
    groupPrev = dummy

    while True:
        kth = getKth(groupPrev, k)
        if not kth:
            break
        groupNext = kth.next

        prev, curr = kth.next, groupPrev.next
        while curr != groupNext:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        tmp = groupPrev.next
        groupPrev.next = kth
        groupPrev = tmp
    return dummy.next

def getKth(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1
    return curr

# ============================
# Test Case [1,2,3,4,5], 3 -> [3,2,1,4,5]
# ============================
if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    
    res = reverseKGroup(a, 3)

    while(res):
        print(res.val)
        res = res.next