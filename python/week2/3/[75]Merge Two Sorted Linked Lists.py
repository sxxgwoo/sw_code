'''
Merge Two Sorted Linked Lists

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted linked list and return the head of the new sorted linked list.

The new list should be made up of nodes from list1 and list2.

Example 1:

Input: list1 = [1,2,4], list2 = [1,3,5]

Output: [1,1,2,3,4,5]

Example 2:

Input: list1 = [], list2 = [1,2]

Output: [1,2]

Example 3:

Input: list1 = [], list2 = []

Output: []
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iteration
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = node = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            node.next = list1
            list1 = list1.next
        else:
            node.next = list2
            list2 = list2.next
        node = node.next

    node.next = list1 or list2

    return dummy.next

# Recursion
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    if list1 is None:
        return list2
    
    if list2 is None:
        return list1
    
    if list1.val <= list2.val:
        list1.next = mergeTwoLists(list1.next, list2)
        return list1
    
    else:
        list2.next = mergeTwoLists(list1, list2.next)
        return list2
    
# ============================
# Test Case [1,2,4], [1,3,5] -> [1,1,2,3,4,5]
# ============================
if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(4)

    a.next = b
    b.next = c

    d = ListNode(1)
    e = ListNode(3)
    f = ListNode(5)

    d.next = e
    e.next = f

    res = mergeTwoLists(a, d)

    while(res):
        print(res.val)

        res = res.next