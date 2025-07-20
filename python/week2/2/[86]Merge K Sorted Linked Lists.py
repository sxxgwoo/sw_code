'''
Merge K Sorted Linked Lists
You are given an array of k linked lists lists, where each list is sorted in ascending order.

Return the sorted linked list that is the result of merging all of the individual linked lists.

Example 1:

Input: lists = [[1,2,4],[1,3,5],[3,6]]

Output: [1,1,2,3,3,4,5,6]
Example 2:

Input: lists = []

Output: []
Example 3:

Input: lists = [[]]

Output: []
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    

    # 1) Brute Force
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        nodes = []
        for lst in lists:
            while lst:
                nodes.append(lst.val)
                lst = lst.next
        nodes.sort()

        res = ListNode(0)
        cur = res
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        return res.next
    
    # 2) Iteration
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        res = ListNode(0)
        cur = res
        
        while True:
            minNode = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minNode == -1 or lists[minNode].val > lists[i].val:
                    minNode = i
            
            if minNode == -1:
                break
            cur.next = lists[minNode]
            lists[minNode] = lists[minNode].next
            cur = cur.next

        return res.next

if __name__ == "__main__":
    sol = Solution()

    # 입력 리스트: lists = [[1,2,4],[1,3,5],[3,6]]
    input_lists = [[1,2,4], [1,3,5], [3,6]]

    # 2D 배열을 연결 리스트 배열로 변환
    def build_linked_list(arr):
        dummy = ListNode()
        cur = dummy
        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next

    linked_lists = [build_linked_list(lst) for lst in input_lists]

    # mergeKLists 실행
    merged = sol.mergeKLists(linked_lists)

    # 결과 출력
    output = []
    while merged:
        output.append(merged.val)
        merged = merged.next
    print(output)
